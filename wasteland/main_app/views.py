from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Item
# Create your views here.


def home(request):
    return render(request, 'home.html')


def items_index(request):
    return render(request, 'items/index.html')


def about(request):
    return render(request, 'about.html')


def characters_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', {'characters': characters})


# def characters_detail(request):
#     characters = Character.objects.get(id=character_id)
