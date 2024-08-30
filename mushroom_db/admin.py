from django.contrib import admin

from mushroom_db.models import Types, Mushrooms, Alphabet

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'en_name': ('name',)}

@admin.register(Mushrooms)
class MushroomsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}

@admin.register(Alphabet)
class AlphabetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('letter',)}