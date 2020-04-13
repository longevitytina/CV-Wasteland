from django import forms
from .models import Item, Character, Situation


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description')


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name', 'location', 'age',
                  'occupation',
                  'intellect', 'toughness', 'speed',
                  'stamina', 'luck', 'strength')


class EditCharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name', 'location', 'age')


# class ResponseForm(forms.ModelForm):
#     class Meta:
#         model = Situation
#         fields = ('response',)
