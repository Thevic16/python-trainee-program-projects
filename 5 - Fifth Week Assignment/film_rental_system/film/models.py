from django.db import models
from django.utils.encoding import smart_text
from film.business_logic import (validator_date_limit_today,
                                 validator_no_negative)
from film.business_logic import FilmBusinessLogic

FILM_TYPE_CHOICES = {
    ('movie', 'Movie'),
    ('serie', 'Serie'),
}


class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return smart_text(self.name)


class Film(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    release_date = models.DateField(validators=[validator_date_limit_today])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2,
                                validators=[validator_no_negative])
    stock = models.IntegerField(validators=[validator_no_negative])
    availability = models.IntegerField(validators=[validator_no_negative])
    film_type = models.CharField(max_length=120, choices=FILM_TYPE_CHOICES)

    film_prequel = models.OneToOneField('self', on_delete=models.CASCADE,
                                        null=True, blank=True)

    def __str__(self):
        return smart_text(self.title)

    def clean(self):
        FilmBusinessLogic. \
            validate_stock_greater_availability(self.stock,
                                                self.availability)
        if self.film_prequel is not None:
            FilmBusinessLogic.validate_film_type_equal_prequel_film_type(
                self.film_type, self.film_prequel.film_type)


class Season(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE,
                             limit_choices_to={'film_type': 'serie'})
    title = models.CharField(max_length=120)
    season_prequel = models.OneToOneField('self', on_delete=models.CASCADE,
                                          null=True, blank=True)

    def __str__(self):
        return smart_text(f"{self.film.title} - {self.title} ")


class Chapter(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    chapter_prequel = models.OneToOneField('self', on_delete=models.CASCADE,
                                           null=True, blank=True)

    def __str__(self):
        return smart_text(f"{self.season.film.title} - {self.season.title}"
                          f" - {self.title} ")
