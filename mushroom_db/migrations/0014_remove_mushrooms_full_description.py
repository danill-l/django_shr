# Generated by Django 5.1 on 2024-08-28 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mushroom_db', '0013_mushrooms_full_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mushrooms',
            name='full_description',
        ),
    ]
