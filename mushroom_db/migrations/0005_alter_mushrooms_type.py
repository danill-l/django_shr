# Generated by Django 5.1 on 2024-08-20 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushroom_db', '0004_alter_mushrooms_description_alter_mushrooms_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mushrooms',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mushroom_db.types', verbose_name='Тип'),
        ),
    ]
