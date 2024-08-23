from django.contrib import admin

from mushroom_articles.models import Article_types, Authors, Articles

# Register your models here.

@admin.register(Authors)
class AuthorURL(admin.ModelAdmin):
    prepopulated_fields = { 'url': ('name',) }


@admin.register(Articles)
class ArticleURL(admin.ModelAdmin):
    prepopulated_fields = { 'url': ('title',) }

@admin.register(Article_types)
class TypeURL(admin.ModelAdmin):
    prepopulated_fields = {'url': ('type',)}