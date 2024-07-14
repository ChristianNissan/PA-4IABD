# Generated by Django 5.0.6 on 2024-07-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appartement', '0009_delete_valeurfonciere_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictionappart',
            name='adresse_code_voie',
            field=models.CharField(choices=[('', '---'), ('ALL', 'Allée'), ('AV', 'Avenue'), ('BD', 'Boulevard'), ('CHE', 'Chemin'), ('RUE', 'Rue'), ('RTE', 'Route'), ('IMP', 'Impasse'), ('QUAI', 'Quai'), ('PL', 'Place'), ('PARC', 'Parc'), ('CRS', 'Cours'), ('RES', 'Résidence'), ('FG', 'Faubourg'), ('VOIE', 'Voie'), ('PTR', 'Porte'), ('PAS', 'Passage'), ('MAIL', 'Mail'), ('SEN', 'Sentier'), ('PTE', 'Petite Rue'), ('TRT', 'Traversée'), ('ZAC', "Zone d'Activité Commerciale"), ('ZI', 'Zone Industrielle')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='predictionappart',
            name='region',
            field=models.CharField(choices=[('', 'Sélectionnez votre région'), ('Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes'), ('Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté'), ('Bretagne', 'Bretagne'), ('Centre-Val de Loire', 'Centre-Val de Loire'), ('Corse', 'Corse'), ('Grand Est', 'Grand Est'), ('Hauts-de-France', 'Hauts-de-France'), ('Île-de-France', 'Île-de-France'), ('Normandie', 'Normandie'), ('Nouvelle-Aquitaine', 'Nouvelle-Aquitaine'), ('Occitanie', 'Occitanie'), ('Pays de la Loire', 'Pays de la Loire'), ("Provence-Alpes-Côte d'Azur", "Provence-Alpes-Côte d'Azur")], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='predictionmaison',
            name='adresse_code_voie',
            field=models.CharField(choices=[('', '---'), ('ALL', 'Allée'), ('AV', 'Avenue'), ('BD', 'Boulevard'), ('CHE', 'Chemin'), ('RUE', 'Rue'), ('RTE', 'Route'), ('IMP', 'Impasse'), ('QUAI', 'Quai'), ('PL', 'Place'), ('PARC', 'Parc'), ('CRS', 'Cours'), ('RES', 'Résidence'), ('FG', 'Faubourg'), ('VOIE', 'Voie'), ('PTR', 'Porte'), ('PAS', 'Passage'), ('MAIL', 'Mail'), ('SEN', 'Sentier'), ('PTE', 'Petite Rue'), ('TRT', 'Traversée'), ('ZAC', "Zone d'Activité Commerciale"), ('ZI', 'Zone Industrielle')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='predictionmaison',
            name='region',
            field=models.CharField(choices=[('', 'Sélectionnez votre région'), ('Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes'), ('Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté'), ('Bretagne', 'Bretagne'), ('Centre-Val de Loire', 'Centre-Val de Loire'), ('Corse', 'Corse'), ('Grand Est', 'Grand Est'), ('Hauts-de-France', 'Hauts-de-France'), ('Île-de-France', 'Île-de-France'), ('Normandie', 'Normandie'), ('Nouvelle-Aquitaine', 'Nouvelle-Aquitaine'), ('Occitanie', 'Occitanie'), ('Pays de la Loire', 'Pays de la Loire'), ("Provence-Alpes-Côte d'Azur", "Provence-Alpes-Côte d'Azur")], default='', max_length=100),
        ),
    ]