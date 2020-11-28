# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from .views import BlogListView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/', BlogListView.as_view()),
]