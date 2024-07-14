# Generated by Django 5.0.6 on 2024-07-02 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appartement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse_postale', models.CharField(max_length=255)),
                ('ville', models.CharField(blank=True, max_length=100)),
                ('code_postal', models.CharField(max_length=5)),
                ('region', models.CharField(choices=[('Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes'), ('Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté'), ('Bretagne', 'Bretagne'), ('Centre-Val de Loire', 'Centre-Val de Loire'), ('Corse', 'Corse'), ('Grand Est', 'Grand Est'), ('Hauts-de-France', 'Hauts-de-France'), ('Île-de-France', 'Île-de-France'), ('Normandie', 'Normandie'), ('Nouvelle-Aquitaine', 'Nouvelle-Aquitaine'), ('Occitanie', 'Occitanie'), ('Pays de la Loire', 'Pays de la Loire'), ("Provence-Alpes-Côte d'Azur", "Provence-Alpes-Côte d'Azur"), ('Outre-Mer', 'Outre-Mer')], max_length=100)),
                ('departement', models.CharField(max_length=100)),
                ('superficie', models.FloatField()),
                ('nombre_de_pieces', models.IntegerField()),
                ('etage', models.IntegerField()),
                ('ascenseur', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse_postale', models.CharField(max_length=255)),
                ('ville', models.CharField(blank=True, max_length=100)),
                ('code_postal', models.CharField(max_length=5)),
                ('region', models.CharField(choices=[('Auvergne-Rhône-Alpes', 'Auvergne-Rhône-Alpes'), ('Bourgogne-Franche-Comté', 'Bourgogne-Franche-Comté'), ('Bretagne', 'Bretagne'), ('Centre-Val de Loire', 'Centre-Val de Loire'), ('Corse', 'Corse'), ('Grand Est', 'Grand Est'), ('Hauts-de-France', 'Hauts-de-France'), ('Île-de-France', 'Île-de-France'), ('Normandie', 'Normandie'), ('Nouvelle-Aquitaine', 'Nouvelle-Aquitaine'), ('Occitanie', 'Occitanie'), ('Pays de la Loire', 'Pays de la Loire'), ("Provence-Alpes-Côte d'Azur", "Provence-Alpes-Côte d'Azur"), ('Outre-Mer', 'Outre-Mer')], max_length=100)),
                ('departement', models.CharField(max_length=100)),
                ('superficie', models.FloatField()),
                ('superficie_terrain', models.FloatField()),
                ('nombre_de_pieces', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PredictionAppart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse_postale', models.CharField(max_length=255)),
                ('code_postal', models.CharField(max_length=10)),
                ('departement', models.CharField(max_length=100)),
                ('superficie', models.FloatField()),
                ('nombre_de_pieces', models.IntegerField()),
                ('etage', models.IntegerField()),
                ('ascenseur', models.BooleanField(default=False)),
                ('prix_estime', models.FloatField()),
                ('date_predicted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
