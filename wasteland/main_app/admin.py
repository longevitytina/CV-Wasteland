from django.contrib import admin
from .models import Character, Item, Situation, ItemAction, Reaction, Log

admin.site.register(Character)
admin.site.register(Item)
admin.site.register(Situation)
admin.site.register(ItemAction)
admin.site.register(Reaction)
admin.site.register(Log)

# Todo
# Customize the Reaction class for a easier to read admin panel
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site
