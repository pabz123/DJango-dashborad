from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework import generics
from .models import Post, Task, Product
from .forms import TaskForm
from .serializers import TaskSerializer


# Function-based views
def dashboard(request):
    context = {
        'posts': Post.objects.all(),
        'tasks': Task.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'dashboard/dashboard.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'dashboard/post_detail.html', {'post': post})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'dashboard/add_task.html', {'form': form})


# API views
class TaskListCreateAPI(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Class-based views
class PostListView(ListView):
    model = Post
    template_name = 'dashboard/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'dashboard/post_detail_cbv.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'dashboard/post_form.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('post-list')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'dashboard/post_form.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('post-list')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'dashboard/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')
