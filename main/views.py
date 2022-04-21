from django.shortcuts import render
from .models import Task, Post
from .forms import TaskForm, PostForm
from rest_framework import viewsets
from .serializers import TaskSerializer, PostSerializer


def index(request):
    tasks = Task.objects.order_by()
    return render(request, 'main/index.html', {
                      'title': 'Главная страница',
                      'header': 'Список дел',
                      'tasks': tasks
                  })


def contacts(request):
    return render(request, 'main/contacts.html')


def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/task.html', context)


def post(request):
    posts = Post.objects.order_by()
    return render(request, 'main/post.html', {
        'title': 'Статьи',
        'header': 'Статьи',
        'posts': posts
    })


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'main/post_creation.html', context)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
