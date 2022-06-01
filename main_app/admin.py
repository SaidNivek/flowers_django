from django.contrib import admin
from .models import Flower # import the Artist model from models.py

# Register your models here.
admin.site.register(Flower) # this line will add the model to the admin panel