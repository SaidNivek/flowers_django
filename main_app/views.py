from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # This will import the class we are extending 
from django.views.generic import DetailView # This will allow us to use the django DetailView
from .models import Flower
from django.urls import reverse # needed by Django to go back to the artist detail page
from django.shortcuts import redirect # needed by Django to redirect after form submission
# import models
from .models import Flower, Seed, Garden # needed to create routes for the seed_create route

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    # Here we have added the playlists as context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gardens"] = Garden.objects.all()
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gardens"] = Garden.objects.all()
        return context

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

class SeedCreate(View):

    def post(self, request, pk):
        seed_type = request.POST.get("seed_type")
        seed_count = request.POST.get("seed_count")
        flower = Flower.objects.get(pk=pk)
        Seed.objects.create(seed_type=seed_type, seed_count=seed_count, flower=flower)
        return redirect('flower_detail', pk=pk)

class GardenFlowerAssoc(View):
    def get(self, request, pk, flower_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Garden.objects.get(pk=pk).flowers.remove(flower_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Garden.objects.get(pk=pk).flowers.add(flower_pk)
        return redirect('home')