from django.db import models

# from biblioteca.applications.libro.models import Book


class Reader(models.Model):
    class Meta:
        db_table = 'reader'

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    nationality = models.CharField('Nacionalidad', max_length=50)
    age = models.PositiveIntegerField('Edad')


class Loan(models.Model):
    class Meta:
        db_table = 'loan'

    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    is_return = models.BooleanField()

    def __str__(self):
        return self.reader
