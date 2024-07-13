from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('movie/<int:movie_id>/', views.display_movie, name='details movies'),
    # path('display_pokemon/<str:pokemon>/', views.display_pokemon, name='display Pokemon')
]

