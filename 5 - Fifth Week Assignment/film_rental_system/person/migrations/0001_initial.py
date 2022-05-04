# Generated by Django 3.2 on 2022-03-14 15:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import film.business_logic


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('gender', models.CharField(choices=[('feminine', 'Feminine'), ('male', 'Male'), ('other', 'Other')], max_length=120)),
                ('date_of_birth', models.DateField(validators=[film.business_logic.validator_date_limit_today])),
                ('person_type', models.CharField(choices=[('film related', 'Film related'), ('client', 'Client')], max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FilmPersonRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.film')),
                ('person', models.ForeignKey(limit_choices_to={'person_type': 'film related'}, on_delete=django.db.models.deletion.CASCADE, to='person.person')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.role')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.TextField()),
                ('phone', models.CharField(max_length=120, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{4}-\\d{4}$')])),
                ('email', models.EmailField(max_length=254)),
                ('person', models.OneToOneField(limit_choices_to={'person_type': 'client'}, on_delete=django.db.models.deletion.CASCADE, to='person.person')),
            ],
        ),
    ]
