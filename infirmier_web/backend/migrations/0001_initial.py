# Generated by Django 5.0.6 on 2024-06-12 09:40

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieDocument',
            fields=[
                ('CodeCategorieDocument', models.AutoField(primary_key=True, serialize=False)),
                ('DesignationCategorie', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cotisation',
            fields=[
                ('CodeCotisation', models.AutoField(primary_key=True, serialize=False)),
                ('Libelle', models.CharField(max_length=200)),
                ('Observation', models.CharField(blank=True, max_length=500, null=True)),
                ('MontantFixe', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrdreInfirmier',
            fields=[
                ('CodeOrdre', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('NumeroOrdre', models.CharField(max_length=100)),
                ('DateObtention', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Periode',
            fields=[
                ('CodePeriode', models.AutoField(primary_key=True, serialize=False)),
                ('DesignationPeriode', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Personnage',
            fields=[
                ('CodePersonnage', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=200)),
                ('Postnom', models.CharField(max_length=200)),
                ('Prenom', models.CharField(max_length=200)),
                ('DateNaissance', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('CodeDocument', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Designation', models.CharField(max_length=200)),
                ('CodeCategorieDocument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.categoriedocument')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('CodePaiement', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('MontantPaye', models.DecimalField(decimal_places=2, max_digits=10)),
                ('DatePaiement', models.DateField()),
                ('Observation', models.CharField(blank=True, max_length=500, null=True)),
                ('CodeCotisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.cotisation')),
                ('CodePeriode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.periode')),
                ('CodePersonnage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.personnage')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentPersonnage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateObtention', models.DateField()),
                ('Valide', models.BooleanField(default=False)),
                ('Url', models.CharField(max_length=300)),
                ('DateEnreg', models.DateField(default=django.utils.timezone.now)),
                ('CodeDocument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.document')),
                ('CodePersonnage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.personnage')),
            ],
        ),
        migrations.CreateModel(
            name='PersonnageOrdre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Active', models.BooleanField(default=False)),
                ('RaisonDesactivation', models.CharField(blank=True, max_length=500, null=True)),
                ('DateDesactivation', models.DateField(blank=True, null=True)),
                ('CodeOrdre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ordreinfirmier')),
                ('CodePersonnage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.personnage')),
            ],
        ),
    ]
