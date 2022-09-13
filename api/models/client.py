from django.db import models

class Client(models.Model):
    phone_phone = models.IntegerField(max_length=255)
    customer_email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    nom_complet = models.CharField(max_length=255)
  
    def __str__(self) -> str:
        return self.nom_complet