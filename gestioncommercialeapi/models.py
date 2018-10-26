# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Permission

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, first_name, last_name, password = None):

        if not email:
            raise ValueError('Users must have a valid email address.')

        email = self.normalize_email(email)
        user = self.model(email = email, first_name = first_name, last_name = last_name)
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, first_name,last_name, password):

        user = self.create_user(email, first_name,last_name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

"""class User(AbstractBaseUser):

    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length = 30, null = True, blank = True)
    last_name = models.CharField( max_length = 30, null = True, blank = True)
    date_joined = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = True)
    updated_by = models.CharField(max_length = 50, null = True, blank = True)
    logo = models.CharField(max_length = 1000000,null = True, blank = True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        
       # Returns the first_name plus the last_name, with a space in between.
        
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


    def get_short_name(self):
        
        #Returns the short name for the user.
        
        return self.first_name


    def __unicode__(self):
        
        return self.email

    def __str__(self):
        
        return self.email"""


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length = 50, null = True, blank = True)
    updated_by = models.CharField(max_length = 50, null = True, blank = True)

    class Meta:
        abstract = True

class Categorie(BaseEntity):

    nom = models.CharField( max_length=30)

class Produit(BaseEntity):

    nom = models.CharField( max_length=50)
    stock = models.IntegerField()
    #prix_vente = models.FloatField()
    categorie = models.ForeignKey(Categorie, related_name='categorie_id', on_delete=models.CASCADE)

    """def __unicode__(self):
        return self.categorie.nom()"""
class Fournisseur(BaseEntity):

    nom = models.CharField( max_length=50)
    prenom = models.CharField( max_length=50)
    tel = models.IntegerField( null = True, blank = True)
    email = models.EmailField()
    adresse = models.CharField( max_length=50, null = True, blank = True)
   

class Approvisionnement(BaseEntity):

    numero = models.CharField(max_length=30, null = True, blank = True)
    #quantite = models.IntegerField()
    #prix_achat = models.FloatField()
    fournisseur = models.ForeignKey(Fournisseur, related_name='fournisseur_id', on_delete=models.CASCADE, null = True, blank = True)

    #produits = models.ManyToManyField(Produit)

class DetailApprovisionnement(BaseEntity):

    numero = models.CharField( max_length=50)
    quantite = models.IntegerField()
    prix_htva = models.FloatField()
    approvisionnement = models.ManyToManyField(Approvisionnement, related_name = 'approvisionnement')
    produit = models.ManyToManyField(Produit, related_name = 'produit')
   
   

class FactureFournisseur(BaseEntity):

    numero = models.CharField( max_length=50)
    approvisionnement = models.ForeignKey(DetailApprovisionnement, related_name='approvisionnement_id', on_delete=models.CASCADE, null = True, blank = True)
    montant = models.FloatField()

class ReglementFournisseur(BaseEntity):
    numero = models.CharField( max_length=50)
    montant_regle = models.FloatField()
    etat = models.CharField( max_length=50)
    facture = models.ForeignKey(FactureFournisseur, related_name='facture_id', on_delete=models.CASCADE)

class Client(BaseEntity):

    nom = models.CharField( max_length=50)
    prenom = models.CharField( max_length=50)
    tel = models.IntegerField( null = True, blank = True)
    email = models.EmailField()
    adresse = models.CharField( max_length=50, null = True, blank = True)

class Commande(BaseEntity):

    numero = models.CharField( max_length=50)
    client = models.ForeignKey(Client, related_name='client_id', on_delete=models.CASCADE, null = True, blank = True)
    #produit = models.ForeignKey(Produit, related_name='produit_id', on_delete=models.CASCADE, null = True, blank = True)
    #produits  = models.ManyToManyField("Produit", related_name="product_item")
    #quantite = models.IntegerField()
    #prix_htva = models.FloatField()

class DetailCommande(BaseEntity):

    numero = models.CharField( max_length=50)
    quantite = models.IntegerField()
    prix_htva = models.FloatField()
    commande = models.ManyToManyField(Commande, related_name = 'commande' )
    produit = models.ManyToManyField(Produit, related_name = 'produit_list')
    #commande = models.ForeignKey(Commande, related_name='commande_id', on_delete=models.CASCADE, null = True, blank = True)
    #produit = models.ForeignKey(Produit, related_name='produit_id', on_delete=models.CASCADE, null = True, blank = True)

class FactureClient(BaseEntity):

    numero = models.CharField( max_length=50)
    commande = models.ForeignKey(DetailCommande, related_name='commande_id', on_delete=models.CASCADE, null = True, blank = True)
    montant = models.FloatField()
class ReglementClient(BaseEntity):

    numero = models.CharField( max_length=50)
    montant_regle = models.FloatField()
    facture = models.ForeignKey(FactureClient, related_name='facture_id', on_delete=models.CASCADE, null = True, blank = True)
    etat = models.CharField( max_length=80)
   

