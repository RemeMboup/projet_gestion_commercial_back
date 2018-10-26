# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-28 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approvisionnement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('nom', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('tel', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('adresse', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(max_length=50)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_id', to='gestioncommercialeapi.Client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetailApprovisionnement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(max_length=50)),
                ('quantite', models.IntegerField()),
                ('prix_htva', models.FloatField()),
                ('approvisionnement', models.ManyToManyField(related_name='approvisionnement', to='gestioncommercialeapi.Approvisionnement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetailCommande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(max_length=50)),
                ('quantite', models.IntegerField()),
                ('prix_htva', models.FloatField()),
                ('commande', models.ManyToManyField(related_name='commande', to='gestioncommercialeapi.Commande')),
                ('produit', models.ManyToManyField(related_name='produit', to='gestioncommercialeapi.Produit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FactureClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(max_length=50)),
                ('montant', models.FloatField()),
                ('commande', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commande_id', to='gestioncommercialeapi.DetailCommande')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FactureFournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(max_length=50)),
                ('montant', models.FloatField()),
                ('approvisionnement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approvisionnement_id', to='gestioncommercialeapi.DetailApprovisionnement')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('tel', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('adresse', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('nom', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie_id', to='gestioncommercialeapi.Categorie')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReglementClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(max_length=50)),
                ('montant_regle', models.FloatField()),
                ('etat', models.CharField(max_length=80)),
                ('facture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='facture_id', to='gestioncommercialeapi.FactureClient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReglementFournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(max_length=50)),
                ('montant_regle', models.FloatField()),
                ('etat', models.CharField(max_length=50)),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facture_id', to='gestioncommercialeapi.FactureFournisseur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='detailcommande',
            name='produit',
            field=models.ManyToManyField(related_name='produit_list', to='gestioncommercialeapi.Produit'),
        ),
        migrations.AddField(
            model_name='detailapprovisionnement',
            name='produit',
            field=models.ManyToManyField(related_name='produit', to='gestioncommercialeapi.Produit'),
        ),
        migrations.AddField(
            model_name='approvisionnement',
            name='fournisseur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fournisseur_id', to='gestioncommercialeapi.Fournisseur'),
        ),
    ]