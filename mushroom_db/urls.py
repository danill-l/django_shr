from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mushroom_db import views

app_name = 'mushroom_db'

urlpatterns = [
    path('', views.list, name='list'),
    path('search/', views.list, name='search'),
    path('types/<slug:mushroom_type>', views.types, name='types'),
    path('mushroom/<slug:mushroom_url>', views.mushroom, name='mushroom'),
    path('alphsearch/<str:first_letter>', views.alphabet, name='alphabet'),
]
