from django.db import models
from biblioteca.applications.autor.models import Author


class Category(models.Model):
    class Meta:
        db_table = 'category'

    name = models.CharField('Nombre', max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        db_table = 'book'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # authors = models.ManyToManyField(Author)
    title = models.CharField('Titulo', max_length=50)
    release_date = models.DateField('Fecha de Lanzamiento')
    front_page = models.ImageField(upload_to='portada')
    visitor_counter = models.PositiveIntegerField('Contador de visitas')

    def __str__(self):
        return self.title
