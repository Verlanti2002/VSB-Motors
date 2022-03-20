import datetime

import os

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return "{}".format(self.nome)

    class Meta:
        db_table = "vsb_app_marca"
        verbose_name_plural = "marche"


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Automobile(models.Model):
    FUEL_CHOICES = (
        (None, "Seleziona"),
        ('Benzina', "Benzina"),
        ('Gasolio', "Gasolio"),
        ('GPL', "GPL"),
        ('Metano', "Metano"),
        ('Elettricità', "Elettricità")
    )

    STATE_CHOICES = (
        (None, "Seleziona"),
        ('Nuovo', "Nuovo"),
        ('Usato', "Usato")
    )

    CHANGE_CHOICES = (
        (None, "Seleziona"),
        ('Manuale', "Manuale"),
        ('Automatico', "Automatico")
    )

    targa = models.CharField(max_length=7, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modello = models.CharField(max_length=100, null=True, blank=True)
    carburante = models.CharField(max_length=100, choices=FUEL_CHOICES, null=True, blank=True)
    cilindrata = models.IntegerField()
    cavalli = models.IntegerField()
    potenza = models.IntegerField()
    stato = models.CharField(max_length=100, choices=STATE_CHOICES, null=True, blank=True)
    km_percorsi = models.IntegerField()
    anno_produzione = models.IntegerField(validators=[MinValueValidator(1900), max_value_current_year])
    numero_proprietari = models.IntegerField()
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    cambio = models.CharField(max_length=100, choices=CHANGE_CHOICES, null=True, blank=True)

    def __str__(self):
        return "Automobile: {}".format(self.targa)

    class Meta:
        db_table = "vsb_app_automobile"
        verbose_name_plural = "automobili"


def get_temp_image_path(instance, filename):
    return os.path.join('images', str(instance.automobile.targa), filename)


class ImmaginiAutomobili(models.Model):
    immagine = models.ImageField(upload_to=get_temp_image_path, blank=True, null=True)
    automobile = models.ForeignKey(Automobile, on_delete=models.CASCADE, related_name='immagini')

    def __str__(self):
        return "ImmaginiAutomobili: {}".format(self.immagine)

    class Meta:
        db_table = "vsb_app_immaginiAutomobili"
        verbose_name_plural = "immagini"