from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('profile/new', views.new_character, name='new_character'),
    path('profile/<int:character_id>/delete/',
         views.delete_character, name='delete_character'),
    path('profile/<int:character_id>/edit/',
         views.edit_character, name='edit_character'),
    path('items/', views.items_list, name='items_list'),
    path('items/<int:item_id>/edit', views.item_edit, name='item_edit'),
    path('profile/<int:character_id>/',
         views.character_detail, name='character_detail'),
    path('profile/<int:character_id>/play',
         views.character_play, name='character_play'),
    path('accounts/', include('django.contrib.auth.urls')),
    #     path('accounts/login/', 'django.contrib.auth.views.login', name='login'),
    #     path('accounts/logout/', 'django.contrib.auth.views.logout', name='logout')
]
