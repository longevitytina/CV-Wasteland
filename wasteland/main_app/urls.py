from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('items/', views.items_list, name='items_list'),
    path('accounts/', include('django.contrib.auth.urls')),

]
