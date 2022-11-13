from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name= 'pages/home.html'

class AboutPageView(TemplateView):
    template_name= 'pages/about.html'

class Dev1(TemplateView):
    template_name = 'pages/dev1.html'

class Dev2(TemplateView):
    template_name= 'pages/dev2.html'

class RTX3060(TemplateView):
    template_name= 'store/rtx3060.html'

class RTX3070(TemplateView):
    template_name= 'store/rtx3070.html'

class RTX3080(TemplateView):
    template_name= 'store/rtx3080.html'