from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def who_coronavirus_update(request):
    webscraper = WebScraper(page="https://www.who.int/emergencies/diseases/novel-coronavirus-2019", element=None)
    response = webscraper.get_page()
    return HttpResponse(response)
