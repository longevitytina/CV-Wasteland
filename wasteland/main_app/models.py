from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


OCCUPATIONS = (
    ('D', 'Doctor'),
    ('L', 'Lumberjack'),
    ('N', 'Ninja'),
    ('U', 'UPS Driver'),
    ('C', 'Card Dealer'),
    ('B', 'Boxer Bodybuilder')
)

ITEM_TYPES = (
    ('W', 'Weapon'),
    ('C', 'Clothing'),
    ('F', 'Food'),
    ('S', 'Shoes'),
    ('B', 'Book'),
    ('T', 'Trinket')
)


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    type = models.CharField(
        max_length=1,
        choices=ITEM_TYPES,
        default=ITEM_TYPES[0][0]
    )

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    age = models.IntegerField()

    occupation = models.CharField(
        max_length=1,
        choices=OCCUPATIONS,
        default=OCCUPATIONS[0][0]
    )

    intellect = models.IntegerField()
    toughness = models.IntegerField()
    speed = models.IntegerField()
    stamina = models.IntegerField()
    luck = models.IntegerField()
    strength = models.IntegerField()

    items = models.ManyToManyField(Item)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"pk": self.id})


class Situation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    # response = models.

    def __str__(self):
        return self.name


class ItemAction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reaction(models.Model):
    name = models.CharField(max_length=100)
    situation_source = models.ForeignKey(
        Situation, related_name='potential_reactions', on_delete=models.CASCADE)
    situation_destination = models.ForeignKey(
        Situation, related_name='previous_reaction', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_action = models.ForeignKey(ItemAction, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Log(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    character = models.ForeignKey(
        Character, related_name='logs', on_delete=models.CASCADE)
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self
