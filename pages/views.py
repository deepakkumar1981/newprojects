from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Pages

# Create your views here.
# pages/views.py


class AboutPageView(TemplateView):
    template_name = 'about.html'


class HomePageView(TemplateView):
    template_name = 'base.html'
    

class ContactUsPageView(TemplateView):
    template_name = 'contactus.html'



