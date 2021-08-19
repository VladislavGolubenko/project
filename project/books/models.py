from django.db import models


class Autor(models.Model):

    name = models.CharField(max_length=250)
    surename = models.CharField(max_length=250)
    fathername = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250)
    birthday = models.DateField()


class Books(models.Model):

    name = models.CharField(max_length=250)
    write_date = models.DateField()
    description = models.CharField(max_length=4000, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='books/%y/%m/%d')
    autor_relative = models.ForeignKey('Autor', on_delete=models.PROTECT, verbose_name='Автор произведения', null=True)
