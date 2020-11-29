from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogModel


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
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')
