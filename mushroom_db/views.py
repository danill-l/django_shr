from django.shortcuts import render
from mushroom_db.models import Types, Mushrooms, Alphabet
from mushroom_db.utils import q_search
# Create your views here.

def list(request):
    
    query = request.GET.get('q', None)
    mushrooms = Mushrooms.objects.all().order_by('name')
    searched = False
    if query:
        mushrooms = q_search(query)
        searched = True

    context = {
        "mushrooms": mushrooms,
        "searched": searched,
    }

    return render(request, 'list.html', context=context)

def types(request, mushroom_type):
     
    mushrooms = Mushrooms.objects.filter(type__en_name=mushroom_type).order_by('name')
    type = mushroom_type
    context = {
        "mushrooms": mushrooms,
        "type": type,
    }

    return render(request, 'list.html', context=context)


def mushroom(request, mushroom_url):

    mushroom = Mushrooms.objects.get(url=mushroom_url)

    context = {
        'mushroom': mushroom,
    }

    return render(request, 'mushroom.html', context=context)

def alphabet(request, first_letter):
    mushrooms = Mushrooms.objects.filter(name__startswith=first_letter)

    context = {
        "mushrooms": mushrooms,
        "first_letter": first_letter,
    }

    return render(request, 'alphabet.html', context=context)