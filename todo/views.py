from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Todo
from .serializer import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filter_fields = ("title", "user", "is_complete")
    search_fields = "title"
    ordering_fields = ("is_complete", "created_at", "updated_at")
