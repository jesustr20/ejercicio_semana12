from django.urls import path
from .import views

urlpatterns = [
    path('list', views.news_list, name='new_list'),
]