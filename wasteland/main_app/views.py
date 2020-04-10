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

# characters index will be in profile page


# def characters_detail(request):
#     characters = Character.objects.get(id=character_id)
#


def profile(request):
    # list of associated characters
    characters = Character.objects.all()
    return render(request, 'profile.html', {'characters': characters})

    # list of associated items
    # user account info
