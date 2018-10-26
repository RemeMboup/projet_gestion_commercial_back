# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from gestioncommercialeapi.serializers import *
from rest_framework.generics import CreateAPIView
from rest_framework_jwt.settings import api_settings

from rest_framework.permissions import IsAdminUser

from django.db.models import Q
from gestioncommercialeapi.models import *
from rest_framework import generics, mixins, status
#from rest_framework.permissions import AllowAny,DjangoModelPermissions
#from rest_framework import permissions

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from rest_framework.response import Response

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

from rest_framework_jwt import views as jwt_views

from django.core.paginator import Paginator

# Create your views here.

"""class CreateUserView(CreateAPIView):


    model = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = self.model.get(username=serializer.data['username'])
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({"message": "User created"
        },
        status=status.HTTP_201_CREATED, headers=headers
        )"""

class UserAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = UserCreateSerializer

    def get_queryset(self):
        qs = User.objects.all()
        email = self.request.GET.get("email")
        if email is not None:
                qs = qs.filter(
                    Q(email__icontains = email)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class UserRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = UserUpdateSerializer

    def get_queryset(self):
        return User.objects.all()



class CategorieAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = CategorieSerializer

    def get_queryset(self):
        qs = Categorie.objects.all()
        #paginator = Paginator(qs, 5)
        nom = self.request.GET.get("nom")
        if nom is not None:
                qs = qs.filter(
                    Q(nom__icontains = nom)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class CategorieRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = CategorieSerializer

    def get_queryset(self):
        return Categorie.objects.all()


class ProduitAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = ProduitSerializer

    def get_queryset(self):
        qs = Produit.objects.all()
        nom = self.request.GET.get("nom")
        if nom is not None:
                qs = qs.filter(
                    Q(nom__icontains = nom)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class ProduitRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = ProduitSerializer

    def get_queryset(self):
        return Produit.objects.all()
class FournisseurAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = FournisseurSerializer

    def get_queryset(self):
        qs = Fournisseur.objects.all()
        nom = self.request.GET.get("nom")
        if nom is not None:
                qs = qs.filter(
                    Q(nom__icontains = nom)
                ).distinct()
        return qs
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class FournisseurRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = FournisseurSerializer

    def get_queryset(self):
        return Fournisseur.objects.all()
class ApprovisionnementAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = ApprovisionnementSerializer

    def get_queryset(self):
        qs = Approvisionnement.objects.all()
        numero = self.request.GET.get("numero")
        if numero is not None:
                qs = qs.filter(
                    Q(numero__icontains = numero)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class ApprovisionnementRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = ApprovisionnementSerializer

    def get_queryset(self):
        return Approvisionnement.objects.all()

class FactureFournisseurAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = FactFournisseurSerializer

    def get_queryset(self):
        qs = FactureFournisseur.objects.all()
        numero = self.request.GET.get("numero")
        if numero is not None:
                qs = qs.filter(
                    Q(numero__icontains = numero)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class FactureFournisseurRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = FactFournisseurSerializer

    def get_queryset(self):
        return FactureFournisseur.objects.all()

class ClientAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = ClientSerializer

    def get_queryset(self):
        qs = Client.objects.all()
        nom = self.request.GET.get("nom")
        if nom is not None:
                qs = qs.filter(
                    Q(nom__icontains = nom)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class ClientRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()

class ReglementFournisseurAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = ReglementFournisseurSerializer

    def get_queryset(self):
        qs = ReglementFournisseur.objects.all()
        numero = self.request.GET.get("numero")
        if numero is not None:
                qs = qs.filter(
                    Q(numero__icontains = numero)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class ReglementFournisseurRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = ReglementFournisseurSerializer

    def get_queryset(self):
        return ReglementFournisseur.objects.all()

class CommandeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = CommandeSerializer

    def get_queryset(self):
        qs = Commande.objects.all()
        numero = self.request.GET.get("numero")
        if numero is not None:
                qs = qs.filter(
                    Q(numero__icontains = numero)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class CommandeRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = CommandeSerializer

    def get_queryset(self):
        return Commande.objects.all()

class FactureClientAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = FactureClientSerializer

    def get_queryset(self):
        qs = FactureClient.objects.all()
        numero = self.request.GET.get("numero")
        if numero is not None:
                qs = qs.filter(
                    Q(numero__icontains = numero)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class FactureClientRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = FactureClientSerializer

    def get_queryset(self):
        return FactureClient.objects.all()

class ReglementClientAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = ReglementClientSerializer

    def get_queryset(self):
        qs = ReglementClient.objects.all()
        numero = self.request.GET.get("numero")
        if numero is not None:
                qs = qs.filter(
                    Q(numero__icontains = numero)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class ReglementClientRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = ReglementClientSerializer

    def get_queryset(self):
        return ReglementClient.objects.all()

class DetailCommandeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """DetailCommande list and create view class"""
    lookup_field = 'id'
    serializer_class = DetailCommandeSerializer

    def get_queryset(self):
        qs = DetailCommande.objects.all()
        numero = self.request.GET.get("numero")
        if numero is not None:
                qs = qs.filter(
                    Q(numero__icontains = numero)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class DetailCommandeRudView(generics.RetrieveUpdateDestroyAPIView):
    """DetailCommandes Retrieve Update and Delete view class"""
    lookup_field = 'id' 
    serializer_class = DetailCommandeSerializer

    def get_queryset(self):
        return DetailCommande.objects.all()




class DetailApprovisionnementAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id' 
    serializer_class = DetailApprovisionnementSerializer

    def get_queryset(self):
        qs = DetailApprovisionnement.objects.all()
        numero = self.request.GET.get("numero")
        if numero is not None:
                qs = qs.filter(
                    Q(numero__icontains = numero)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class DetailApprovisionnementRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = DetailApprovisionnementSerializer

    def get_queryset(self):
        return DetailApprovisionnement.objects.all()


