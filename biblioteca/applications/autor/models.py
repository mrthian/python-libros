from django.db import models


# Create your models here.
class Author(models.Model):
    class Meta:
        db_table = 'author'

    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    nationality = models.CharField('Nacionalidad', max_length=50)
    edad = models.PositiveIntegerField('Edad')

    def __str__(self):
        return f"Author: {self.first_name} {self.last_name}"
