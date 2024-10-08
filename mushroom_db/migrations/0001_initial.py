# Generated by Django 5.1 on 2024-08-20 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Mushrooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.CharField(max_length=120)),
                ('latin', models.CharField(max_length=50)),
                ('syn', models.CharField(max_length=120, null=True)),
                ('description', models.TextField()),
                ('is_it_good', models.CharField(max_length=50)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mushroom_db.types')),
            ],
        ),
    ]
