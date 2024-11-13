from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Главная страница'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': text
    }
    return render(request, template, context)


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse(f'Публикации групп: {slug}')


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Группы'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text
    }
    return render(request, template, context)
