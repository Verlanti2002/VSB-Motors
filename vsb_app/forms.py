import datetime

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import Automobile, ImmaginiAutomobili, Marca, current_year


def year_choices():
    return [(r, r) for r in range(1900, datetime.date.today().year+1)]


class AutomobileForm(forms.ModelForm):

    targa = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Inserire la targa'}))
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), widget=forms.Select, empty_label="Seleziona la marca")
    modello = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Inserire il modello'}))
    carburante = forms.ChoiceField(choices=Automobile.FUEL_CHOICES, widget=forms.Select)
    cilindrata = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire la cilindrata'}))
    cavalli = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire i cavalli'}))
    potenza = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire la potenza'}))
    stato = forms.ChoiceField(choices=Automobile.STATE_CHOICES, widget=forms.Select)
    km_percorsi = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire i kilometri percorsi'}))
    anno_produzione = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year, widget=forms.Select)
    numero_proprietari = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire il numero di proprietari'}))
    prezzo = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Inserire il prezzo'}))
    cambio = forms.ChoiceField(choices=Automobile.CHANGE_CHOICES, widget=forms.Select)

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


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):

        super(LoginForm, self).__init__(*args, **kwargs)
