from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.client import Client
from .models.produit import Produit
from .serializers.client import ClientSerializer
from .serializers.produits import ProduitSerializer
from rest_framework import status
  
@api_view(['GET','POST'])
def clients(request):
    if request.method == 'GET':
        # checking for the parameters from the URL
        if request.query_params:
            items = Client.objects.filter(**request.query_param.dict())
        else:
            items = Client.objects.all()
            serializer = ClientSerializer(items, many=True)
    
        # if there is something in items else raise error
        if items:
            return Response(serializer.data)
        else:
            return Response([])

    elif request.method == 'POST':
        item = ClientSerializer(data=request.data)
        # validating for already existing data

        # ex_client = Client.objects.all().filter(email = request.data['email'])
        # if ex_client:
        #     return Response('Email déja utilisé',status=status.HTTP_409_CONFLICT)
    
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            return Response(['user_name', 'email', 'password'],status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def produits(request):
    if request.method == 'GET':
        # checking for the parameters from the URL
        if request.query_params:
            items = Produit.objects.filter(**request.query_param.dict())
        else:
            items = Produit.objects.all()
            serializer = ProduitSerializer(items, many=True)
    
        # if there is something in items else raise error
        if items:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        item = ProduitSerializer(data=request.data)
        # validating for already existing data

        ex_produit = Produit.objects.all().filter(name = request.data['name'])
        if ex_produit:
            return Response(request.data['name']+' existe déja',status=status.HTTP_409_CONFLICT)
        if item.is_valid():
            item.save()
            return Response(item.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

