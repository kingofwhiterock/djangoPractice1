# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/', BlogListView.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('delete/', BlogDeleteView.as_view(), name='delete'),
]