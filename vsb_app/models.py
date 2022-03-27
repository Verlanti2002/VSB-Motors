import datetime

import os

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .managers import CustomUserManager


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
    data_registrazione = models.DateTimeField(default=timezone.now)

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


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Concessionaria(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ragione_sociale = models.CharField(max_length=100, unique=True)
    partita_IVA = models.CharField(max_length=11, unique=True)
    indirizzo = models.CharField(max_length=100, null=True, blank=True)
    citta = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return "Concessionaria: {}".format(self.ragione_sociale)

    class Meta:
        db_table = "vsb_app_concessionaria"
        verbose_name_plural = "concessionarie"


class Ordine(models.Model):
    data = models.DateTimeField(default=timezone.now)
    automobile = models.ForeignKey(Automobile, on_delete=models.CASCADE)
    acquirente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return "Ordine: Acq({}) Aut({})".format(self.acquirente.pk, self.automobile.pk)

    class Meta:
        db_table = "vsb_app_ordine"
        verbose_name_plural = "ordini"
        unique_together = ('data', 'automobile', 'acquirente')
