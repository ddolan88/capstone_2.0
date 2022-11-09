from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name= 'pages/home.html'

class AboutPageView(TemplateView):
    template_name= 'pages/about.html'

class Dev1View(TemplateView):
    template_name = 'pages/dev1.html'

class Dev2View(TemplateView):
    template_name= 'pages/dev2.html'