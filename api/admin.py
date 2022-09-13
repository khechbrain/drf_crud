from django.contrib import admin
from .models.produit import Produit
from .models.client import Client

# Register your models here.
admin.site.register(Client)
admin.site.register(Produit)