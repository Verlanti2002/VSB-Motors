import datetime

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import Automobile, ImmaginiAutomobili, Marca, current_year


def year_choices():
    return [(r, r) for r in range(1950, datetime.date.today().year+1)]


class AutomobileForm(forms.ModelForm):

    targa = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Inserire la targa'}))
    stato = forms.ChoiceField(choices=Automobile.STATE_CHOICES, widget=forms.Select)
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), widget=forms.Select, empty_label="Seleziona la marca")
    modello = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Inserire il modello'}))
    cavalli = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire i cavalli'}))
    potenza = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire la potenza'}))
    alimentazione = forms.CharField(widget=forms.TextInput(attrs={'value': 'Elettrico'}))
    km_percorsi = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire i kilometri percorsi'}))
    anno_immatricolazione = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year, widget=forms.Select)
    numero_proprietari = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire il numero di proprietari'}))
    prezzo = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire il prezzo'}))
    cambio = forms.ChoiceField(choices=Automobile.CHANGE_CHOICES, widget=forms.Select)
    tipologie_di_uso = forms.ChoiceField(choices=Automobile.USED_CHOICES, widget=forms.Select)
    numero_marce = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire il numero di marce'}))
    neopatentato = forms.ChoiceField(choices=Automobile.NEW_DRIVER_CHOICES, widget=forms.Select)
    consumo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Inserire il consumo'}))
    classe_emissioni = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire la classe di emissione'}))
    emissioni_CO2 = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire la quantità di emissioni di CO2'}))
    colore = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Inserire il colore'}))
    carrozzeria = forms.ChoiceField(choices=Automobile.CAR_BODY_CHOICES, widget=forms.Select)
    peso_a_vuoto = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire il peso a vuoto'}))
    porte = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire il numero di porte'}))
    posti = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire il numero di posti'}))

    class Meta:
        model = Automobile
        fields = [
            "targa",
            "stato",
            "marca",
            "modello",
            "cavalli",
            "potenza",
            "alimentazione",
            "km_percorsi",
            "anno_immatricolazione",
            "numero_proprietari",
            "prezzo",
            "cambio",
            "tipologie_di_uso",
            "numero_marce",
            "neopatentato",
            "consumo",
            "classe_emissioni",
            "emissioni_CO2",
            "colore",
            "carrozzeria",
            "peso_a_vuoto",
            "porte",
            "posti"
        ]


class ImmaginiAutomobiliForm(forms.ModelForm):

    immagine = forms.ImageField(label='Immagine', widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = ImmaginiAutomobili
        fields = ['immagine']


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):

        super(LoginForm, self).__init__(*args, **kwargs)
