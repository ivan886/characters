from django.contrib import admin

# Register your models here.
from django.contrib import admin
from characters.models import Character, Universe

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description')
    list_display_links = ('id', 'name')


@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'foundation')
    list_display_links = ('id', 'name')