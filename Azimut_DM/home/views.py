from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.all()
    return render(request, 'home/index.html', {'news': news, 'title': 'Новость'})
