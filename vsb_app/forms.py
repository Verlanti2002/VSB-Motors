import datetime

from django import forms
from .models import Automobile, ImmaginiAutomobili, Marca, current_year


def year_choices():
    return [(r, r) for r in range(1900, datetime.date.today().year+1)]


class AutomobileForm(forms.ModelForm):

    targa = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_box'}))
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), widget=forms.Select(attrs={'class': 'input_box'}), empty_label="Seleziona")
    modello = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_box'}))
    carburante = forms.ChoiceField(choices=Automobile.FUEL_CHOICES, widget=forms.Select(attrs={'class': 'input_box'}))
    cilindrata = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input_box'}))
    cavalli = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input_box'}))
    potenza = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input_box'}))
    stato = forms.ChoiceField(choices=Automobile.STATE_CHOICES, widget=forms.Select(attrs={'class': 'input_box'}))
    km_percorsi = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input_box'}))
    anno_produzione = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year, widget=forms.Select(attrs={'class': 'input_box'}))
    numero_proprietari = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input_box'}))
    prezzo = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'input_box'}))
    cambio = forms.ChoiceField(choices=Automobile.CHANGE_CHOICES, widget=forms.Select(attrs={'class': 'input_box'}))

    class Meta:
        model = Automobile
        fields = [
            "targa",
            "marca",
            "modello",
            "carburante",
            "cilindrata",
            "cavalli",
            "potenza",
            "stato",
            "km_percorsi",
            "anno_produzione",
            "numero_proprietari",
            "prezzo",
            "cambio"
        ]


class ImmaginiAutomobiliForm(forms.ModelForm):

    immagine = forms.ImageField(label='Immagine', widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = ImmaginiAutomobili
        fields = ['immagine']

