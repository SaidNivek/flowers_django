from django.contrib import admin
from .models import Flower, Seed, Garden # import the Artist model from models.py

# Register your models here.
admin.site.register(Flower) # this line will add the model to the admin panel
admin.site.register(Seed) # this line will add the model to the admin panel
admin.site.register(Garden) # this line will add the model to the admin panel