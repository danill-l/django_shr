# Generated by Django 5.1 on 2024-08-28 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mushroom_db', '0015_mushroomsdesc_mushrooms_full_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MushroomsDesc',
        ),
    ]
