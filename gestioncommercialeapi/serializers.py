from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from gestioncommercialeapi.serializers import *
from gestioncommercialeapi.models import *

"""class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user"""

class UserCreateSerializer(serializers.ModelSerializer):
    """User Create Serializer class"""


    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
            ]

    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    """User Update Serializer class"""


    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'password',
            ]


class CategorieSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model = Categorie
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model = Produit
        fields = '__all__'

class FournisseurSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model = Fournisseur
        fields = '__all__'
        
class ApprovisionnementSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model = Approvisionnement
        fields = '__all__'

class FactFournisseurSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model = FactureFournisseur
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model = Client
        fields = '__all__'

class ReglementFournisseurSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model = ReglementFournisseur
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model = Commande
        fields = '__all__'

class FactureClientSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model = FactureClient
        fields = '__all__'
 
class ReglementClientSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model = ReglementClient
        fields = '__all__'

"""class DetailCommandeSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model =  DetailCommande
        fields = '__all__'"""
class DetailCommandeSerializer(serializers.ModelSerializer):
    """DetailCommande Write Serializer class"""
    class Meta:
        model = DetailCommande
        fields = '__all__'


class DetailApprovisionnementSerializer(serializers.ModelSerializer):
    """Categorie Serializer class"""
    class Meta:
        model =  DetailApprovisionnement
        fields = '__all__'