from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('profile/new', views.new_character, name='new_character'),
    path('items/', views.items_list, name='items_list'),
    path('items/<int:item_id>/edit', views.item_edit, name='item_edit'),
    path('profile/<int:character_id>/',
         views.character_detail, name='character_detail'),
    path('accounts/', include('django.contrib.auth.urls'))

]
