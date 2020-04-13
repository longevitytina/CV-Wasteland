from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Character, Item, Reaction, Log
from .forms import ItemForm, CharacterForm, EditCharacterForm, ReactionForm
from django.contrib.auth.forms import UserCreationForm


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
    form = ReactionForm(request.POST)
    character = Character.objects.get(id=character_id)
    logs = character.logs.all()
    current_situation = logs.last().reaction.situation_destination

    if request.method == 'POST':
        if form.is_valid():
            new_reaction = form.save(commit=False)
            reaction = Reaction.objects.get(
                name=new_reaction.name, situation_source_id=current_situation.id)
            Log.objects.create(character_id=character_id,
                               reaction_id=reaction.id)
        return redirect('character_play', character_id)

    context = {
        'character': character,
        'logs': logs,
        'current_situation': current_situation,
        'form': form
    }

    return render(request, 'characters/character_play.html', context)


def delete_character(request, character_id):
    Character.objects.get(id=character_id).delete()
    return redirect('profile')


def edit_character(request, character_id):
    character = Character.objects.get(id=character_id)

    if request.method == 'POST':
        form = EditCharacterForm(request.POST, instance=character)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            return redirect('character_detail', character.id)
    else:
        form = EditCharacterForm()
        context = {'form': form}
        return render(request, 'characters/character_form.html', context)

    return redirect('edit_character')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
