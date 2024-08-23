from django.shortcuts import render
from django.http import HttpRequest, HttpResponseNotFound, HttpResponse, HttpResponseRedirect
# from mushroom_list.mushrooms import Mushroom, MushroomBuilder, MushroomsContainer
# from mushroom_list.database import DBConnect, PGMushroomsManager
# Create your views here.



def list(request):
    template = 'list.html'
    return render(request, template)


# def list(request: HttpRequest):
#     connect = DBConnect.get_connect(dbname='library',
#                                     host='localhost',
#                                     port=5432,
#                                     user='postgres',
#                                     password='postgres')

#     cursor = connect.cursor()
#     query = """ SELECT * FROM mushrooms """
#     cursor.execute(query)
#     container = MushroomsContainer()
#     container.create_list_mushrooms(cursor.fetchall())
#     data = container.get_list_mushrooms()
#     count = len(data) if data is not None else 0
#     cursor.close()

#     cursor = connect.cursor()
#     query = """ SELECT type_name, translation FROM types """
#     cursor.execute(query)
#     types = {item[0]: "http://127.0.0.1:8000/list/list/" + item[1] + '/' for item in cursor.fetchall()}
#     cursor.close()

#     context = {
#         "data": data,
#         "count": count,
#         "types": types,
#     }

#     return render(request, template_name='list.html', context=context)

