from django import template

from mushroom_db.models import Types
from mushroom_articles.models import Article_types, Sliders

register = template.Library()

@register.simple_tag
def tag_types():
    return Types.objects.all()

@register.simple_tag
def tag_article_type():
    return Article_types.objects.all()

@register.simple_tag
def tag_slider_images():
    return Sliders.objects.all()