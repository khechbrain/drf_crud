from django.db.models import fields
from rest_framework import serializers
from ..models.produit import Produit
  
class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ('name', 'description', 'total_amount')