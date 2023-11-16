from django.db import models
from django.utils.text import slugify


class Human(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    favorite_music = models.CharField(max_length=50)
    favorite_hobbies = models.CharField(max_length=50)
    favorite_anime = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, blank=True)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.name} - {self.surname} - {self.age}')
        super(Human, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f'{self.name} - {self.age}'

    def get_absolute_url(self):
        return f'{self.pk}'


class RegHuman(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.PositiveIntegerField()
    favorite_music = models.CharField(max_length=50)
    favorite_hobbies = models.CharField(max_length=255)
    favorite_anime = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.surname} - {self.age} - {self.address} - {self.favorite_music} - ' \
               f'{self.favorite_hobbies} - {self.favorite_anime}'