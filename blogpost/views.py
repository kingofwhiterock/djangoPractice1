from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import BlogModel

FIELD = ('title', 'content', 'category')


# Create your views here.
class BlogListView(ListView):
    template_name = 'list.html'
    model = BlogModel


class BlogDetailView(DetailView):
    template_name = 'detail.html'
    model = BlogModel


class BlogCreateView(CreateView):
    template_name = 'create.html'
    model = BlogModel
    fields = FIELD
    success_url = reverse_lazy('list')


class BlogDeleteView(DeleteView):
    template_name = 'delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')


class BlogUpdateView(UpdateView):
    template_name = 'update.html'
    model = BlogModel
    fields = FIELD
    success_url = reverse_lazy('list')