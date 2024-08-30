from django.db.models import Q

from mushroom_db.models import Mushrooms


def q_search(query):
    if query.isdigit() and len(query) <=5:
        return Mushrooms.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) >= 1]

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(name__icontains = token)
    
    return Mushrooms.objects.filter(q_objects)