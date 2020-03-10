from rest_framework import serializers
from .models import Customers, Sidelki

class CustomersSerializer(serializers.ModelSerializer):
    class Meta():
        model = Customers
        fields =['fio','diagnoz','vozrast','nachato','zaversheno','predoplata','price','telefon1','telefon2']


class SidelkiSerializer(serializers.ModelSerializer):
    class Meta():
        model = Sidelki
        fields = ['fio','strana','vozrast','v_bolnitse','prihodiashaya','prozhivaet','ozhidaet','telefon1','medic','adres_proziv']