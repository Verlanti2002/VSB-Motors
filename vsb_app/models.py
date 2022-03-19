from django.db import models


# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return "Marca: {}".format(self.nome)

    class Meta:
        db_table = "vsb_app_marca"
        verbose_name_plural = "marche"


class Automobile(models.Model):
    FUEL_CHOICES = (
        ('B', "Benzina"),
        ('D', "Gasolio"),
        ('G', "GPL"),
        ('M', "Metano"),
        ('E', "Elettricità")
    )

    STATE_CHOICES = (
        ('N', "Nuovo"),
        ('U', "Usato")
    )

    targa = models.CharField(max_length=6, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    carburante = models.CharField(max_length=1, choices=FUEL_CHOICES)
    cilindrata = models.IntegerField()
    cavalli = models.IntegerField()
    potenza = models.IntegerField()
    stato = models.CharField(max_length=1, choices=STATE_CHOICES)
    km_percorsi = models.IntegerField()
    anno_produzione = models.DateField()
    numero_proprietari = models.IntegerField()
    prezzo = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Automobile: {}".format(self.targa)

    class Meta:
        db_table = "vsb_app_automobile"
        verbose_name_plural = "automobili"


class ImmaginiAutomobili(models.Model):
    immagine = models.ImageField(upload_to="images/%Y/%m/%d")
    automobile = models.ForeignKey(Automobile, on_delete=models.CASCADE, related_name='immagini')

    def __str__(self):
        return "ImmaginiAutomobili: {}".format(self.immagine)

    class Meta:
        db_table = "vsb_app_immaginiAutomobili"
        verbose_name_plural = "immagini"