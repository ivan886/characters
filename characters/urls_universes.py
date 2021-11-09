from django.contrib import admin
from django.urls import path
from . import  views_universes

app_name = "universes"

urlpatterns = [
    path('', views_universes.list, name="list_universes"),
    path('save', views_universes.save, name="save_universes"),


]
