from django.contrib import admin

from mushroom_db.models import Types, Mushrooms

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'en_name': ('name',)}

@admin.register(Mushrooms)
class MushroomsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}