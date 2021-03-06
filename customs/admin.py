from django.contrib import admin
from .models import Customers, Sidelki

# Register your models here.

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['fio','diagnoz','vozrast','nachato','zaversheno','predoplata','price','rezume']
    search_fields = ['telefon1','telefon2','diagnoz','opisanie_bolnoy','fio']


@admin.register(Sidelki)
class SidelkiAdmin(admin.ModelAdmin):
    list_display = ['fio','strana','vozrast','v_bolnitse','prihodiashaya','prozhivaet','ozhidaet','telefon1','medic','zapolneno']
    search_fields = ['strana','list_ozidanie','fio']