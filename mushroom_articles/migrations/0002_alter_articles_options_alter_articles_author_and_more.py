# Generated by Django 5.1 on 2024-08-22 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushroom_articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Статью', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mushroom_articles.authors', verbose_name='Автор у этой статьи'),
        ),
        migrations.AlterField(
            model_name='authors',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Имя автора'),
        ),
    ]
