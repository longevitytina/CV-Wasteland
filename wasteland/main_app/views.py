from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Character, Item, Log
from .forms import ItemForm, CharacterForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def items_list(request):
    items = Item.objects.all()
    return render(request, 'main_app/item_list.html', {'items': items})


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
    characters = Character.objects.filter(user=request.user)
    print()
    # user account info
    username = request.user
    context = {
        'username': username,
        'characters': characters
    }

    return render(request, 'profile.html', context)


def item_edit(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('items_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'main_app/item_form.html', {'form': form})


def new_character(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)

            character.user = request.user
            character.save()
            return redirect('character_detail', character.id)
    else:
        form = CharacterForm()
    context = {'form': form}
    return render(request, 'characters/character_form.html', context)


def character_play(request, character_id):
    character = Character.objects.get(id=character_id)
    log = character.logs.first()
    print(log)
    # print(character.logs.all())
    # print(character.logs.first().reaction.situation_source)
    context = {
        'character': character,
        'log': log,
    }

    return render(request, 'characters/character_play.html', context)
