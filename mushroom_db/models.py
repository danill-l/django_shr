from django.db import models

# Create your models here.

class Types(models.Model):

    name = models.CharField(max_length=120, null=False, verbose_name='Название типа')
    en_name = models.SlugField(max_length=120, unique=True, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'types'
        verbose_name: str = 'Тип'
        verbose_name_plural: str ='Типы'
    
    def display_name(self):
        return self.name


class Mushrooms(models.Model):

    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображение')
    name = models.CharField(max_length=150, verbose_name='Название')
    latin = models.CharField(max_length=150, verbose_name='Название на латыни')
    syn = models.CharField(max_length=150, blank=True, null=True, verbose_name='Синонимы')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    extras = models.CharField(max_length=150, blank=True, null=True, verbose_name='Примечания')
    url = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    full_description = models.TextField(blank=True, null=True, verbose_name='Полное описание')
    type = models.ForeignKey('Types', on_delete=models.CASCADE, verbose_name='Тип')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'mushrooms'
        verbose_name: str = 'Гриб'
        verbose_name_plural: str = 'Грибы'

    def display_id(self):
        return self.id

class Alphabet(models.Model):
    letter = models.CharField(max_length=2, null=False, verbose_name='Заглавная буква')
    url = models.SlugField(max_length=120, unique=True, blank=True, null=True, verbose_name='URL')
    
    def __str__(self):
        return self.letter
    
    class Meta:
        db_table = 'alphabet'
        verbose_name: str = 'Алфавит'
        verbose_name_plural: str = 'Алфавиты'