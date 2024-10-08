# Generated by Django 5.1 on 2024-08-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushroom_db', '0007_alter_mushrooms_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='types',
            name='en_name',
            field=models.SlugField(blank=True, max_length=120, null=True, unique=True, verbose_name='URL'),
        ),
    ]
