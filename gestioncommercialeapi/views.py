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
import psycopg2
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
conn = psycopg2.connect("host=127.0.0.1 dbname=commercial_gestion user=postgres password=Pass@123 port=5433")
from datetime import timedelta,time
import datetime
import requests
import json

def get_facture(id):
    response = requests.get('http://localhost:8000/factclient/'+str(id)+ '/')
    to_return = json.loads(response.content)
    return to_return

"""def get_detail_commande(numero):
    response = requests.get('http://localhost:8000/detail-commande-create/?numero='+str(numero)+ '/')
    to_return = json.loads(response.content)

    return to_return
print(get_detail_commande("0000016"))"""
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
                    Q(numero__iexact = numero)
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
                    Q(numero__iexact = numero)
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
                    Q(numero__iexact = numero)
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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommandeSerializer
        return CommandesSerializer

    def get_queryset(self):
        qs = Commande.objects.all()
        numero = self.request.GET.get("numero")
        if numero is not None:
                qs = qs.filter(
                    Q(numero__iexact = numero)
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

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FactureClientSerializer
        return FactureClientReadSerializer

    def get_queryset(self):
        qs = FactureClient.objects.all()
        numero = self.request.GET.get("numero")
        if numero is not None:
                qs = qs.filter(
                    Q(numero__iexact = numero)
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
                    Q(numero__iexact = numero)
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
                    Q(numero__iexact = numero)
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
                    Q(numero__iexact = numero)
                ).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class DetailApprovisionnementRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field = 'id' 
    serializer_class = DetailApprovisionnementSerializer

    def get_queryset(self):
        return DetailApprovisionnement.objects.all()


class AddFactureClientView(APIView):
    def post(self, request, format=None):
        facture_client_serializer = FactureClientSerializer(data=request.data)
        montant = 0
        list_somme = []
        if facture_client_serializer.is_valid():
            print(facture_client_serializer.data['commande'])
            for i in facture_client_serializer.data['commande']:
                idc = i
                print(idc)
                resp = DetailCommande.objects.filter(Q(id = idc))
                print(resp)
                if len(resp.values()) > 0:
                    print(resp.values())
                    iddcommande = resp.values()[0]['id']
                    numerodcommande = resp.values()[0]['numero']
                    quantitedcommande = resp.values()[0]['quantite']
                    prixdcommande = resp.values()[0]['prix_htva']
                    montant_t = quantitedcommande * prixdcommande
                    montant += montant_t
                    print(montant)
                    fc = FactureClient(numero = facture_client_serializer.data['numero'], montant= montant )
                    fc.save(force_insert= True)
                    print(fc)
                    fc_id = fc.id
                    print(fc_id)
            for i in facture_client_serializer.data['commande']:
                idc = i
                print(idc)
                resp = DetailCommande.objects.filter(Q(id = idc))
                print(resp)
                if len(resp.values()) > 0:
                    print(resp.values())
                    iddcommande = resp.values()[0]['id']
                    sql ="""Insert Into gestioncommercialeapi_factureclient_commande(factureclient_id, detailcommande_id)
                    values (%s,%s)"""
                    data =  fc_id , iddcommande
                    print('Mareme')
                    print(fc_id)
                    print('Mboup')
                    print(data)
                    cur = conn.cursor()
                    cur.execute(sql,data)
                    conn.commit()
                    cur.close()
                    """get_fact = get_facture(fc_id)
                    print(get_fact)
                    l = []
                    for i in get_fact["commande"]:
                        montant = i["quantite"] * i["prix_htva"]
                        l.append(montant)
                        print(l)
                    montant_total = sum(l)
                    print(montant_total)"""
                    sql ="""Update gestioncommercialeapi_factureclient SET montant = '{}' where id= {}""".format(montant, fc_id)
                    print(sql)
                    cur = conn.cursor()
                    cur.execute(sql)
                    conn.commit()
                    cur.close()
            return Response({"status": "succes"},status=status.HTTP_200_OK)
        else:
            return Response(facture_client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetDetailCommandeView(APIView):
    
    def post(self, request, format=None):
        get_detCommande_serializer = GetDetailCommandeSerializer(data=request.data)
        montant = 0
        if get_detCommande_serializer.is_valid():
            resp = Commande.objects.filter(Q(numero = get_detCommande_serializer.data['numero'] ))
            if len(resp.values()) > 0:
                rep_list = resp.values()[0]['id']
                print(rep_list)
                client_id = resp.values()[0]['client_id']
                client_detail = Client.objects.filter(Q(id =  client_id))
                print(client_detail)
                print(client_detail.values()[0])
                detail_commande = DetailCommande.objects.filter(Q(commande = rep_list))
                list_detail_commande = detail_commande.values()
                print(list_detail_commande)
                n_list = []
                new_list = {}
                montant_total = 0
                
                for i in list_detail_commande:
                    num = i['numero']
                    print('Soda')
                    print(num)
                    i['montant'] = i['quantite'] * i['prix_htva']
                    n_list.append(i)
                    montant_total+= i['montant']
                    montant +=  montant_total
                    #detail_com = get_detail_commande(Q(numero = num))
                    #sql ="""Select * gestioncommercialeapi_detail_commande_produit where produit_id = {}""".format()
            
                    detail_com = DetailCommande.objects.filter(Q(numero = num))
                    detail = detail_com.values()
                    print(detail)
                    print('mareme')
                    print(detail_com)
                    print('mareme')
                    #produit_id= detail_com.values()[0]['produit']
                    #print(produit_id)
                    #produit = Produit.objects.filter(Q(id = produit_id))
                    #produit_name = produit.values()[0]['nom']
                    #print(produit_name)
                    print(montant)
                    #i['produit'] = produit_name
                    
                    #i['client']  = client_detail.values()[0]
                new_list['Detail_Commande'] = n_list
                new_list['client']  =  client_detail.values()[0]  
                new_list['Montant'] = montant
                #print(montant_total)
                    
                
                return Response(new_list,status=status.HTTP_200_OK)
            else:
                return Response([],status=status.HTTP_200_OK)
        else:
            return Response(get_detCommande_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddDetailCommandeView(APIView):
    
    def post(self, request, format=None):
        detail_commande_serializer = DetailCommandeSerializer(data=request.data)

        if detail_commande_serializer.is_valid():
            for i in detail_commande_serializer.data['produit']:
                idp = i
                print(idp)
                resp = Produit.objects.filter(Q(id = idp))
                print(resp)
                if len(resp.values()) > 0:
                    print(resp.values())
                    idproduit = resp.values()[0]['id']
                    id_produit = Produit.objects.filter(Q(id = idproduit))
                    print("mareme")
                    print(id_produit)
                    print("mboup")
                    print(id_produit.values()[0]['stock'])
                    print("ok")
            for j in detail_commande_serializer.data['commande']:
                idc = j
                print(idc)
                resp1= Commande.objects.filter(Q(commande = idc))
                if len(resp1.values()) > 0:
                    print(resp1.values())
                    idcommande = resp1.values()[0]['id']
                    id_commande = Commande.objects.filter(Q(id = idcommande))
                    print("mareme")
                    print(id_commande)
            if detail_commande_serializer.data['quantite'] > id_produit.values()[0]['stock']:
                #raise Exception('La quantite saisi nest pas disponible')
                return Response({'La quantite saisi nest pas disponible'},status=status.HTTP_200_OK)
            else:
                dc  = DetailCommande(numero = detail_commande_serializer.data['numero'], quantite = detail_commande_serializer.data['quantite'], prix_htva = detail_commande_serializer.data['prix_htva'])
                print(dc)
                dc.save(force_insert= True)
                print(dc)
                dc_id = dc.id
                print('m')
                sql ="""Insert Into gestioncommercialeapi_detailcommande_commande(detailcommande_id, commande_id)
                values (%s,%s)"""
                data =  dc_id , idcommande
                print(data)
                cur = conn.cursor()
                cur.execute(sql,data)
                conn.commit()
                cur.close()

                sql ="""Insert Into gestioncommercialeapi_detailcommande_produit(detailcommande_id, produit_id)
                values (%s,%s)"""
                data =  dc_id , idproduit
                print(data)
                cur = conn.cursor()
                cur.execute(sql,data)
                conn.commit()
                cur.close()

                new_stock = id_produit.values()[0]['stock'] - detail_commande_serializer.data['quantite'] 
                sql ="""Update gestioncommercialeapi_produit SET stock = '{}' where id= {}""".format(new_stock, idproduit)
                print(sql)
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()
                cur.close()

                return Response({'Sucess'},status=status.HTTP_200_OK)
            return Response({'Sucess'},status=status.HTTP_200_OK)
        else:
            return Response(detail_commande_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class AddDetailApprovisionnementView(APIView):
    
    def post(self, request, format=None):
        detail_appro_serializer = DetailApprovisionnementSerializer(data=request.data)

        if detail_appro_serializer.is_valid():
            for i in detail_appro_serializer.data['produit']:
                idp = i
                print(idp)
                resp = Produit.objects.filter(Q(id = idp))
                print(resp)
                if len(resp.values()) > 0:
                    print(resp.values())
                    idproduit = resp.values()[0]['id']
                    id_produit = Produit.objects.filter(Q(id = idproduit))
                    print("mareme")
                    print(id_produit)
                    print("mboup")
                    print(id_produit.values()[0]['stock'])
                    print("ok")
            for j in detail_appro_serializer.data['approvisionnement']:
                idc = j
                print(idc)
                resp1= Approvisionnement.objects.filter(Q(approvisionnement = idc))
                if len(resp1.values()) > 0:
                    print(resp1.values())
                    idcommande = resp1.values()[0]['id']
                    id_commande = Commande.objects.filter(Q(id = idcommande))
                    print("mareme")
                    print(id_commande)
            
                    dc  = DetailApprovisionnement(numero = detail_appro_serializer.data['numero'], quantite = detail_appro_serializer.data['quantite'], prix_htva = detail_appro_serializer.data['prix_htva'])
                    print(dc)
                    dc.save(force_insert= True)
                    print(dc)
                    dc_id = dc.id
                    print('m')
                    sql ="""Insert Into gestioncommercialeapi_detailapprovisionnement_approvisionnement(detailapprovisionnement_id, approvisionnement_id)
                    values (%s,%s)"""
                    data =  dc_id , idcommande
                    print(data)
                    cur = conn.cursor()
                    cur.execute(sql,data)
                    conn.commit()
                    cur.close()

                    sql ="""Insert Into gestioncommercialeapi_detailapprovisionnement_produit(detailapprovisionnement_id, produit_id)
                    values (%s,%s)"""
                    data =  dc_id , idproduit
                    print(data)
                    cur = conn.cursor()
                    cur.execute(sql,data)
                    conn.commit()
                    cur.close()

                    new_stock = id_produit.values()[0]['stock'] + detail_appro_serializer.data['quantite'] 
                    sql ="""Update gestioncommercialeapi_produit SET stock = '{}' where id= {}""".format(new_stock, idproduit)
                    print(sql)
                    cur = conn.cursor()
                    cur.execute(sql)
                    conn.commit()
                    cur.close()

                    return Response({'Sucess'},status=status.HTTP_200_OK)
                return Response({'Sucess'},status=status.HTTP_200_OK)
        else:
            return Response(detail_commande_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



