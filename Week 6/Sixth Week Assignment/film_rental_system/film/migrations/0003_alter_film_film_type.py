# Generated by Django 3.2 on 2022-03-10 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_alter_film_film_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='film_type',
            field=models.CharField(choices=[('movie', 'Movie'), ('serie', 'Serie')], max_length=120),
        ),
    ]
