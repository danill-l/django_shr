# from abc import ABC, abstractmethod
# from .mushrooms import Mushroom, MushroomsContainer
# import psycopg2

# class DBConnect:

#     _instance = None

#     @classmethod
#     def get_connect(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = psycopg2.connect(*args, **kwargs)
#         return cls._instance

# class DBManager(ABC):

#     @staticmethod
#     @abstractmethod
#     def create(connect, mushroom: Mushroom):
#         ...

#     @staticmethod
#     @abstractmethod
#     def read(connect, mushroom: Mushroom):
#         ...

#     @staticmethod
#     @abstractmethod
#     def update(connect, old_mushroom: Mushroom, new_mushroom: Mushroom):
#         ...

#     @staticmethod
#     @abstractmethod
#     def delete(connect, mushroom: Mushroom):
#         ...

# class PGMushroomsManager(DBManager):

#     @staticmethod
#     def create(connect, mushroom: Mushroom):
#         # Вызвать запрос вставки данных из объекта в таблицу
#         ...

#     @staticmethod
#     def read(connect, mushroom: Mushroom) -> list[Mushroom]:

#         try:
#             with connect.cursor() as cursor:

#                 params = (mushroom.name, )
#                 query = """SELECT * 
#                            FROM mushrooms
#                            WHERE name = %s"""
#                 cursor.execute(query, params)
#                 data = cursor.fetchall()

#                 if data:
#                     container = MushroomsContainer()
#                     container.create_list_mushrooms(data)
#                     return container.get_list_mushrooms()
#                 else:
#                     raise Exception(f"Не найдена запись с параметрами {params}")
#         except (Exception, psycopg2.Error) as e:
#             print(e)

#     @staticmethod
#     def update(connect, index_old_mushroom: int, new_mushroom: Mushroom):
#         # Обновить данные о книге в таблице
#         ...

#     @staticmethod
#     def delete(connect, mushroom: Mushroom):
#         # Удалить девайс
#         ...
