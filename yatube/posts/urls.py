from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Страница со списком групп
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
    # Главная страница
    path('', views.index, name='index'),
    path('group_list/', views.group_list, name='group_list')
]
