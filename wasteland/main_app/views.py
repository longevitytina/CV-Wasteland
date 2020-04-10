from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Item
# Create your views here.


def home(request):
    return HttpResponse('<h1>CV-WASTELAND /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def items_index(request):
    return render(request, 'items/index.html')

def about(request):
    return render(request, 'about.html')

def characters_index(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', { 'characters': characters })
