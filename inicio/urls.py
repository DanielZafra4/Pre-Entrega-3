from django.urls import path
from inicio.views import (
    inicio,
    crear_pokemon,
    buscar_pokemon,
    about_me
)

app_name = "inicio"

urlpatterns = [
    path('', inicio, name="inicio"),
    path('buscar-pokemon/', buscar_pokemon, name="buscar_pokemon"),
    path('crear-pokemon/', crear_pokemon, name="crear_pokemon"),
    path('about-me/', about_me, name="about_me")  
]
