from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('items/', views.items_list, name='items_list'),
    path('profile/<int:character_id>/',
         views.character_detail, name='character_detail'),
    # path('profile/<int:charcter_id>/assoc_item/<int:item_id>/',
    #      views.assoc_item, name='assoc_item'),
    path('accounts/', include('django.contrib.auth.urls'))

]
