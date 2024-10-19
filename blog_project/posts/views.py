from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
  model = Post
  template_name = "posts/home.html"


class PostDetailView(DetailView):
  model = Post
  template_name = "posts/post_detail.html"

class PostCreateView(CreateView): # new
  model = Post
  template_name = "posts/post_new.html"
  fields = ["title", "author", "content"]
  success_url = reverse_lazy('home')

class PostUpdateView(UpdateView):
  model = Post
  template_name = "posts/post_edit.html"
  fields = ['title', 'content']
  success_url = reverse_lazy('home')


class PostDeleteView(DeleteView):
  model = Post
  template_name = "posts/post_delete.html"
  success_url = reverse_lazy('home')



