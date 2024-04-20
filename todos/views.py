from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TodoItem, ProLicense
from .forms import TodoItemForm, RegistrationForm
from django.contrib.auth import login

@login_required
def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

@login_required
def todo_detail(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            pro_license = ProLicense.objects.filter(user=user).first()
            if pro_license and pro_license.is_pro:
                todo_item = form.save(commit=False)
                todo_item.user = user
                todo_item.save()
                return redirect('todo_list')
            else:
                return render(request, 'todos/no_pro_license.html')
    else:
        form = TodoItemForm()
    return render(request, 'todos/todo_form.html', {'form': form})

@login_required
def todo_update(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            user = request.user
            pro_license = ProLicense.objects.filter(user=user).first()
            if pro_license and pro_license.is_pro:
                form.save()
                return redirect('todo_list')
            else:
                return render(request, 'todos/no_pro_license.html')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form})

@login_required
def todo_delete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('todo_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# views.py

def buy_pro_license(request):
    # Logic to handle the purchase of a pro license
    return render(request, 'todos/buy_pro_license.html')  # Replace with your actual template

