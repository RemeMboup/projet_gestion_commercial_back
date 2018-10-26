"""backendgestioncommercial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin



from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
import gestioncommercialeapi
from gestioncommercialeapi.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get-token/$', obtain_jwt_token),
    url(r'^verify-token/', verify_jwt_token),
    url(r'^user-create/', UserAPIView.as_view()),
    url(r'^user/(?P<id>\d+)/', UserRudView.as_view()),
    url(r'^categorie-create/', CategorieAPIView.as_view()),
    url(r'^categorie/(?P<id>\d+)/', CategorieRudView.as_view()),
    url(r'^produit-create/', ProduitAPIView.as_view()),
    url(r'^produit/(?P<id>\d+)/', ProduitRudView.as_view()),
    url(r'^fournisseur-create/', FournisseurAPIView.as_view()),
    url(r'^fournisseur/(?P<id>\d+)/', FournisseurRudView.as_view()),
    url(r'^approvisionnement-create/', ApprovisionnementAPIView.as_view()),
    url(r'^approvisionnement/(?P<id>\d+)/', ApprovisionnementRudView.as_view()),
    url(r'^factfournisseur-create/', FactureFournisseurAPIView.as_view()),
    url(r'^factfournisseur/(?P<id>\d+)/', FactureFournisseurRudView.as_view()),
    url(r'^client-create/', ClientAPIView.as_view()),
    url(r'^client/(?P<id>\d+)/', ClientRudView.as_view()),
    url(r'^regle-fourniseur-create/', ReglementFournisseurAPIView.as_view()),
    url(r'^regle-fourniseur/(?P<id>\d+)/', ReglementFournisseurRudView.as_view()),
    url(r'^commande-create/', CommandeAPIView.as_view()),
    url(r'^commande/(?P<id>\d+)/', CommandeRudView.as_view()),
    url(r'^factclient-create/', FactureClientAPIView.as_view()),
    url(r'^factclient/(?P<id>\d+)/', FactureClientRudView.as_view()),
    url(r'^regle-client-create/', ReglementClientAPIView.as_view()),
    url(r'^regle-client/(?P<id>\d+)/', ReglementClientRudView.as_view()),
    url(r'^detail-commande-create/', DetailCommandeAPIView.as_view()),
    url(r'^detail-commande/(?P<id>\d+)/', DetailCommandeRudView.as_view()),
    url(r'^detail-appros-create/', DetailApprovisionnementAPIView.as_view()),
    url(r'^detail-appros/(?P<id>\d+)/', DetailApprovisionnementRudView.as_view()),
    
]
