from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Character, Item
from .forms import ItemForm
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


def assoc_item(request, character_id, item_id):
    Character.objects.get(id=character_id).items.add(item_id)
    return redirect('character_detail', character_id=character_id)


def profile(request):
    # list of associated characters
    characters = Character.objects.filter(user=request.user)
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
