from django.shortcuts import render

from mushroom_articles.models import Articles


# Create your views here.
def article(request, article_type):
    articles = Articles.objects.filter(type__url=article_type).order_by('title')
    name_of_url = article_type
    context = {
        "articles": articles,
        "name_of_url": name_of_url,
    }
    return render(request, 'article.html', context=context)

def article_full(request, article_url):
    individual_article = Articles.objects.get(url=article_url)

    context = {
        "individual_article": individual_article,
    }
    return render(request, 'article_full.html', context=context)