# Generated by Django 4.0.4 on 2024-07-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_remove_film_author_remove_film_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]