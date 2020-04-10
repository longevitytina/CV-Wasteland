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
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 100)
    type = models.CharField(
        max_length = 1,
        choices = ITEM_TYPES,
        default = ITEM_TYPES[0][0]
    )

    def __str__ (self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    age = models.IntegerField()
    starting_date = models.DateField('Starting Date')

    occupation = models.CharField(
        max_length = 1,
        choices = OCCUPATIONS,
        default = OCCUPATIONS[0][0]
    )

    intellect = models.IntegerField()
    toughness = models.IntegerField()
    speed = models.IntegerField()
    stamina = models.IntegerField()
    luck = models.IntegerField()
    strength = models.IntegerField()

    items = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"pk": self.id})





# Create your models here.
