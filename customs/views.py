from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class List(View):
    def get(self, request):
            return HttpResponse("This's a page of the customers_list one")

def homepage(request):
    return HttpResponse("This's a homepage of the data_lists")
