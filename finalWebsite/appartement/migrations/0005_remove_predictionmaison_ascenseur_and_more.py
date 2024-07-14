# Generated by Django 5.0.6 on 2024-07-03 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appartement', '0004_predictionappart_predictionmaison_delete_appartement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictionmaison',
            name='ascenseur',
        ),
        migrations.RemoveField(
            model_name='predictionmaison',
            name='etage',
        ),
        migrations.AlterField(
            model_name='predictionappart',
            name='region',
            field=models.CharField(choices=[('Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes'), ('Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté'), ('Bretagne', 'Bretagne'), ('Centre-Val de Loire', 'Centre-Val de Loire'), ('Corse', 'Corse'), ('Grand Est', 'Grand Est'), ('Hauts-de-France', 'Hauts-de-France'), ('Île-de-France', 'Île-de-France'), ('Normandie', 'Normandie'), ('Nouvelle-Aquitaine', 'Nouvelle-Aquitaine'), ('Occitanie', 'Occitanie'), ('Pays de la Loire', 'Pays de la Loire'), ("Provence-Alpes-Côte d'Azur", "Provence-Alpes-Côte d'Azur")], max_length=100),
        ),
        migrations.AlterField(
            model_name='predictionmaison',
            name='region',
            field=models.CharField(choices=[('Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes'), ('Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté'), ('Bretagne', 'Bretagne'), ('Centre-Val de Loire', 'Centre-Val de Loire'), ('Corse', 'Corse'), ('Grand Est', 'Grand Est'), ('Hauts-de-France', 'Hauts-de-France'), ('Île-de-France', 'Île-de-France'), ('Normandie', 'Normandie'), ('Nouvelle-Aquitaine', 'Nouvelle-Aquitaine'), ('Occitanie', 'Occitanie'), ('Pays de la Loire', 'Pays de la Loire'), ("Provence-Alpes-Côte d'Azur", "Provence-Alpes-Côte d'Azur")], max_length=100),
        ),
    ]