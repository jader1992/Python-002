from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Name


def index(request):
    return HttpResponse('Hello world!')


def year(request, year):
    # return HttpResponse(year)
    return redirect("/2020.html")  # 重新跳转到路由文件


def name(request, **kwargs):
    return HttpResponse(kwargs['name'] + str(kwargs['year']))


def myyear(request, year):
    return render(request, 'yearview.html')


def books(request):
    books = Name.objects.all()
    return render(request, 'books.html', locals())  # locals获取所有的本地变量
