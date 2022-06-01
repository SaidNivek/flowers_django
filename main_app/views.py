from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Flower

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class FlowerList(TemplateView):
    template_name = "flower_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["flowers"] = Flower.objects.all() # this is where we add the key into our context object for the view to use
        return context
