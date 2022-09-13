from django.db import models

class Produit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    total_amount = models.IntegerField(max_length=255)
  
    def __str__(self) -> str:
        return self.name