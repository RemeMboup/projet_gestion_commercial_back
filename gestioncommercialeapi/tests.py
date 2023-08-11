# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import requests
import json
# Create your tests here.

def get_facture(id):
    response = requests.get('http://localhost:8000/factclient/'+str(id)+ '/')
    to_return = json.loads(response.content)
    return to_return

#print(get_facture(65))

def get_detail_commande(numero):
    response = requests.get('http://localhost:8000/detail-commande-create/?numero='+numero+'/')
    print(response)
    to_return = json.loads(response.content)

    return to_return
print(get_detail_commande('000001'))
