# Generated by Django 4.0.4 on 2024-06-24 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='TmdbFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.user')),
            ],
        ),
    ]