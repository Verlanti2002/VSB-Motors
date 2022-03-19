from django.contrib import admin
from .models import Automobile, Marca, ImmaginiAutomobili
# Register your models here.


class AutomobileAdmin(admin.ModelAdmin):
    pass


class MarcaAdmin(admin.ModelAdmin):
    pass


class ImmaginiAutomobiliAdmin(admin.ModelAdmin):
    pass


admin.site.register(Automobile, AutomobileAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(ImmaginiAutomobili, ImmaginiAutomobiliAdmin)
