# from abc import ABC, abstractmethod


# class Mushroom:

#     def __init__(self):

#         self.name = None
#         self.type = None
#         self.latin = None
#         self.syn = None
#         self.description = None
#         self.sys = None
#         self.picture = None


# class Builder(ABC):

#     @abstractmethod
#     def create(self):
#         ...

#     @abstractmethod
#     def set_name(self, name):
#         ...
    
#     @abstractmethod
#     def set_type(self, type):
#         ...

#     @abstractmethod
#     def set_latin(self, latin):
#         ...

#     @abstractmethod
#     def set_syn(self, syn):
#         ...

#     @abstractmethod
#     def set_description(self, description):
#         ...

#     @abstractmethod
#     def set_sys(self, sys):
#         ...

#     @abstractmethod
#     def set_picture(self, picture):
#         ...

#     @abstractmethod
#     def get_mushroom(self):
#         ...

# class MushroomBuilder(Builder):

#     _mushroom: Mushroom

#     def create(self):
#         self._mushroom = Mushroom()

#     def set_name(self, name):
#         self._mushroom.name = name

#     def set_type(self, type):
#         self._mushroom.type = type
    
#     def set_latin(self, latin):
#         self._mushroom.latin = latin

#     def set_syn(self, syn):
#         self._mushroom.syn = syn

#     def set_description(self, description):
#         self._mushroom.description = description

#     def set_sys(self, sys):
#         self._mushroom.sys = sys

#     def set_picture(self, picture):
#         self._mushroom.picture = picture

#     def get_mushroom(self):
#         return self._mushroom

# class MushroomCreator:

#     def __init__(self, builder: Builder):
#         self.builder = builder
    
#     def change_builder(self, builder: Builder):
#         self._builder = builder

#     def make(self, mushroom: tuple) -> Mushroom:
#         self._builder.create()
#         self._builder.set_name(mushroom[1])
#         self.builder.set_type(mushroom[2])
#         self._builder.set_latin(mushroom[3])
#         self._builder.set_syn(mushroom[4])
#         self._builder.set_description(mushroom[5])
#         img_path = str(mushroom[6]) + '.jpg'
#         self._builder.set_picture(img_path)
#         return self._builder.get_mushroom()

# class MushroomsContainer:

#     def __init__(self):
#         self._mushrooms: list[Mushroom] = []

#     def create_list_mushrooms(self, data: list):

#         builder = MushroomBuilder()
#         creator = MushroomCreator(builder)

#         for record in data:
#             mushroom = creator.make(record)
#             self._mushrooms.append(mushroom)
    
#     def add_mushroom(self, mushroom: Mushroom):
#         self._mushrooms.append(mushroom)

#     def get_list_mushrooms(self):
#         return self._mushrooms