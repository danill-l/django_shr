from django import template

from mushroom_db.models import Types
from mushroom_articles.models import Article_types

register = template.Library()

@register.simple_tag
def tag_types():
    return Types.objects.all()

@register.simple_tag
def tag_article_type():
    return Article_types.objects.all()