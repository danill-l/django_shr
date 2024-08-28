from django.db import models

# Create your models here.

class Article_types(models.Model):
    type = models.CharField(max_length=120, null=False, verbose_name='Название типа статьи')
    url = models.SlugField(max_length=120, unique=True, blank=True, null=True, verbose_name='URL')
    
    def __str__(self):
        return self.type

    class Meta:
        db_table = 'article_types'
        verbose_name: str = 'Тип статьи'
        verbose_name_plural: str ='Типы статей'

    # def display_type(self):
    #     return self.type

class Authors(models.Model):
    name = models.CharField(max_length=120, null=False, verbose_name='Имя автора')
    url = models.SlugField(max_length=120, unique=True, blank=True, null=True, verbose_name='URL')
 
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'
        verbose_name: str = 'Автора'
        verbose_name_plural: str = 'Авторы'

class Articles(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    article_image = models.ImageField(upload_to='article_image/', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание статьи')
    url = models.SlugField(max_length=120, unique=True, blank=True, null=True, verbose_name='URL')
    author = models.ForeignKey('Authors', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автор у этой статьи')
    type = models.ForeignKey('Article_types', on_delete=models.CASCADE, verbose_name='Тип статьи')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'articles'
        verbose_name: str = 'Статью'
        verbose_name_plural: str = 'Статьи'

class Sliders(models.Model):
    name = models.CharField(max_length=120, null=False, verbose_name='Имя картинки для слайдера')
    image = models.ImageField(upload_to='slider_images/', blank=True, null=True, verbose_name='Изображение для слайдера')
    type = models.ForeignKey('Article_types', on_delete=models.CASCADE, verbose_name='Тип статьи, для которой сделана картинка')
    url = models.SlugField(max_length=120, unique=True, blank=True, null=True, verbose_name='URL')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'slider_images'
        verbose_name: str = 'Картинку'
        verbose_name_plural: str = 'Картинки'