from django.contrib import admin
from .models import Automobile, Marca, ImmaginiAutomobili, CustomUser, Concessionaria
# Register your models here.


class AutomobileAdmin(admin.ModelAdmin):
    pass


class MarcaAdmin(admin.ModelAdmin):
    pass


class ImmaginiAutomobiliAdmin(admin.ModelAdmin):
    pass


class ConcessionariaAdmin(admin.ModelAdmin):
    pass


class CustomUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Automobile, AutomobileAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(ImmaginiAutomobili, ImmaginiAutomobiliAdmin)
admin.site.register(Concessionaria, ConcessionariaAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
