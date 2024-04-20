import graphene
from graphene_django.types import DjangoObjectType
from .models import TodoItem

class TodoItemType(DjangoObjectType):
    class Meta:
        model = TodoItem

class Query(graphene.ObjectType):
    all_todo_items = graphene.List(TodoItemType)

    def resolve_all_todo_items(root, info):
        return TodoItem.objects.all()

schema = graphene.Schema(query=Query)
