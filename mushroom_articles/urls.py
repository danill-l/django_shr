from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mushroom_articles import views


app_name = 'mushroom_articles'

urlpatterns = [
    path('<slug:article_type>', views.article, name='article'),
]
