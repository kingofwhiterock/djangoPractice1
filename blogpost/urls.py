# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView, BlogUpdateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/', BlogListView.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
]