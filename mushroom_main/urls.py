
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mushroom_main import views

app_name = 'mushroom_main'

urlpatterns = [
    path('', views.index, name='index'),
    path('faq/', views.faq, name = 'faq'),
    path('rules/', views.rules, name = 'rules'),
    path('about/', views.about, name = 'about'),
]
