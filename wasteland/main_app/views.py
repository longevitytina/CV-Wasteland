from django.shortcuts import render
from django.http import HttpResponse
from .models import Character, Item
# Create your views here.


def home(request):
    return render(request, 'home.html')


def items_list(request):
    return render(request, 'main_app/item_list.html')


def about(request):
    return render(request, 'about.html')

def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    items_character_doesnt_have = Item.objects.exclude(
        id__in=character.items.all().values_list('id'))

    context = {
        'character': character,
        'items': items_character_doesnt_have
    }
    return render(request, 'characters/detail.html', context)

def profile(request):
    # list of associated characters
    characters = Character.objects.all()
    return render(request, 'profile.html', {'characters': characters})
    # user account info
