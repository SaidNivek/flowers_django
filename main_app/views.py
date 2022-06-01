from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # This will import the class we are extending 
from django.views.generic import DetailView # This will allow us to use the django DetailView
from .models import Flower
from django.urls import reverse # needed by Django to go back to the artist detail page

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
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["flowers"] = Flower.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["flowers"] = Flower.objects.all()
            # default header for not searching 
            context["header"] = "Trending Flowers"
        return context

class FlowerCreate(CreateView):
    model = Flower
    fields = ['name', 'image', 'description']
    template_name = "flower_create.html"
    success_url = "/flowers/"

        # this will get the pk from the route and redirect to artist view
    def get_success_url(self):
        return reverse('flower_detail', kwargs={'pk': self.object.pk})

class FlowerDetail(DetailView):
    model = Flower
    template_name = "flower_detail.html"

class FlowerUpdate(UpdateView):
    model = Flower
    fields = ['name', 'image', 'description']
    template_name = "flower_update.html"
    succes_url = "/flowers/"

    def get_success_url(self):
        return reverse('flower_detail', kwargs={'pk': self.object.pk})

class FlowerDelete(DeleteView):
    model = Flower
    template_name = "flower_delete_confirmation.html"
    success_url = "/flowers/"