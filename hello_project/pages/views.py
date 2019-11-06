from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, template_name='home.html', context={})


def menu_page(request):
    return render(request, template_name='menu.html', context={})


def pl_words_page(request):
    return render(request, template_name='pl_words.html', context={})
