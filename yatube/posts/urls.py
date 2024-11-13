from django.urls import path
from . import views

urlpatterns = [
    # Страница со списком групп
    path('group/<slug:slug>/', views.group_posts),
    # Главная страница
    path('', views.index),
    path('group_list/', views.group_list)
]
