"""
URL configuration for TodoListProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from todos.views import register  # Import the register view
from todos.views import buy_pro_license
from graphene_django.views import GraphQLView
from todos.schema import schema  # Adjust the import statement here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', register, name='register'),  # Add this line for registration
    path('buy_pro_license/', buy_pro_license, name='buy_pro_license'),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)), 
]

