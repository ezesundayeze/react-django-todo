from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer
from django.views.decorators.csrf import ensure_csrf_cookie


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class=TaskSerializer