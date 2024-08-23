from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from mushroom_db.models import Types
from mushroom_db.models import Mushrooms
from mushroom_articles.models import Articles, Article_types
# Create your views here.


def index(request):
    article_types = Articles.objects.filter(type__url = 'stati-o-gribah')
    mushrooms = Mushrooms.objects.all()
    cook_articles = Articles.objects.filter(type__url = 'recepty-s-gribami')
    cook = cook_articles
    count_of_meals = 0
    counter = 0
    counter_for_articles = 0

    for meal in cook:
        count_of_meals +=1
    for mushroom in mushrooms:
        counter += 1
    for article in article_types:
        counter_for_articles +=1
    
    context = {
        "mushrooms":mushrooms,
        "counter": counter,
        "counter_for_articles": counter_for_articles,
        "article_types": article_types,
        "meals": count_of_meals,
    }

    return render(request, 'main/index.html', context=context)





def faq(request):
    template = 'main/faq.html'
    return render(request, template)
def rules(request):
    template = 'main/rules.html'
    return render(request, template)
def about(request):
    template = 'main/about.html'
    return render(request, template)
def list(request):
    template = 'list.html'
    return render(request, template)