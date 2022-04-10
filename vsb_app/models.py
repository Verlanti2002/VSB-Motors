import datetime

import os

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    is_client = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return "{}".format(self.nome)

    class Meta:
        db_table = "vsb_app_marca"
        verbose_name_plural = "marche"


class Concessionaria(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ragione_sociale = models.CharField(max_length=100, unique=True)
    partita_IVA = models.CharField(max_length=11, unique=True)
    indirizzo = models.CharField(max_length=100, null=True, blank=True)
    citta = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "Concessionaria: {}".format(self.ragione_sociale)

    class Meta:
        db_table = "vsb_app_concessionaria"
        verbose_name_plural = "concessionarie"


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Automobile(models.Model):

    STATE_CHOICES = (
        (None, "Seleziona lo stato"),
        ('Nuovo', "Nuovo"),
        ('Usato', "Usato")
    )

    USED_CHOICES = (
        (None, "Seleziona la tipologia d'uso"),
        ('Privato', "Privato"),
        ('Aziendale', "Aziendale"),
        ('Iva esposta', "Iva esposta")
    )

    NEW_DRIVER_CHOICES = (
        (None, "Neopatentato"),
        ('Si', "Si"),
        ('No', "No")
    )

    TRACTION_CHOICES = (
        (None, "Seleziona la trazione"),
        ('Anteriore', "Anteriore"),
        ('Posteriore', "Posteriore"),
        ('Integrale', "Integrale")
    )

    CAR_BODY_CHOICES = (
        (None, "Seleziona la carrozzeria"),
        ('Berlina', "Berlina"),
        ('Station Wagon', "Station Wagon"),
        ('SUV', "SUV"),
        ('Coupè', "Coupè"),
        ('Cabrio', "Cabrio")
    )

    targa = models.CharField(max_length=7, unique=True)
    stato = models.CharField(max_length=100, choices=STATE_CHOICES, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modello = models.CharField(max_length=100, null=True, blank=True)
    cavalli = models.IntegerField()
    potenza = models.IntegerField()
    alimentazione = models.CharField(max_length=100, null=True, blank=True)
    km_percorsi = models.CharField(max_length=100, null=True, blank=True)
    anno_immatricolazione = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1950), max_value_current_year
    ])
    numero_proprietari = models.IntegerField()
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    tipologie_di_uso = models.CharField(max_length=100, choices=USED_CHOICES, null=True, blank=True)
    neopatentato = models.CharField(max_length=100, choices=NEW_DRIVER_CHOICES, null=True, blank=True)
    consumo = models.CharField(max_length=100, null=True, blank=True)
    batteria = models.CharField(max_length=100, null=True, blank=True)
    colore = models.CharField(max_length=100, null=True, blank=True)
    trazione = models.CharField(max_length=100, choices=TRACTION_CHOICES, null=True, blank=True)
    carrozzeria = models.CharField(max_length=100, choices=CAR_BODY_CHOICES, null=True, blank=True)
    peso_a_vuoto = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(500), MaxValueValidator(3000)
    ])
    porte = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(3), MaxValueValidator(5)])
    posti = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(2), MaxValueValidator(5)])
    data_registrazione = models.DateTimeField(default=timezone.now)
    concessionaria = models.ForeignKey(Concessionaria, on_delete=models.CASCADE, related_name='automobile')
    is_purchased = models.BooleanField(default=False)

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


class Ordine(models.Model):
    data = models.DateTimeField(default=timezone.now)
    automobile = models.ForeignKey(Automobile, on_delete=models.CASCADE, related_name='ordine')
    acquirente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ordine')

    def __str__(self):
        return "Ordine: Acq({}) Aut({})".format(self.acquirente.pk, self.automobile.pk)

    class Meta:
        db_table = "vsb_app_ordine"
        verbose_name_plural = "ordini"
        unique_together = ('data', 'automobile', 'acquirente')
