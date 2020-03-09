from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from  rest_framework import viewsets
from .serializers import CustomersSerializer, SidelkiSerializer
from .models import Customers, Sidelki

class List(View):
    def get(self, request):
            return HttpResponse("This's a page of the customers_list one")

def homepage(request):
    return HttpResponse("This's a homepage of the data_lists")


class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()


class SidelkiViewSet(viewsets.ModelViewSet):
    serializer_class = SidelkiSerializer
    queryset = Sidelki.objects.all()