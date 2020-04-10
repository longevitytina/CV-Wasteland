from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('items/', views.items_list, name='items_list'),
    path('profile/<int:character_id>/', views.character_detail, name='character_detail'),
    path('accounts/', include('django.contrib.auth.urls')),

]
