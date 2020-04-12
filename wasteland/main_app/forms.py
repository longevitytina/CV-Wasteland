from django import forms
from .models import Item, Character


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description')


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name', 'location', 'age',
                  'starting_date', 'occupation',
                  'intellect', 'toughness', 'speed',
                  'stamina', 'luck', 'strength')
