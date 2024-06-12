from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class Personnage(models.Model):
    CodePersonnage = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nom = models.CharField(max_length=200)
    Postnom = models.CharField(max_length=200)
    Prenom = models.CharField(max_length=200)
    DateNaissance = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

    
class OrdreInfirmier(models.Model):
    CodeOrdre = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    NumeroOrdre = models.CharField(max_length=100)
    DateObtention = models.DateField()


class PersonnageOrdre(models.Model):
    CodePersonnageOrdre = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CodePersonnage = models.ForeignKey(Personnage, related_name='list_personnage_ordre', on_delete=models.CASCADE)
    CodeOrdre = models.ForeignKey(OrdreInfirmier,  related_name='list_personnage_ordre',on_delete=models.CASCADE)
    Active = models.BooleanField(default=False)
    RaisonDesactivation = models.CharField(max_length=500, null=True, blank=True)
    DateDesactivation = models.DateField(null=True, blank=True)

    
class CategorieDocument(models.Model):
    CodeCategorieDocument = models.AutoField(primary_key=True)
    DesignationCategorie = models.CharField(max_length=200, null=False, blank=False)


class Document(models.Model):
    CodeDocument = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CodeCategorieDocument = models.ForeignKey(CategorieDocument, on_delete=models.CASCADE, related_name='list_documents')
    Designation = models.CharField(max_length=200,null=False, blank=False)
    

class DocumentPersonnage(models.Model):
    CodeDocumentPersonnage = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CodeDocument = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='list_document_personnage')
    CodePersonnage = models.ForeignKey(Personnage, on_delete=models.CASCADE, related_name='list_document_personnage')
    DateObtention = models.DateField()
    Valide = models.BooleanField(default=False)
    Url = models.CharField(max_length=300, null=False, blank=False)
    DateEnreg = models.DateTimeField(default=timezone.now)


class Cotisation(models.Model):
    CodeCotisation =  models.AutoField(primary_key=True)
    Libelle = models.CharField(max_length=200, null=False, blank=False)
    Observation = models.CharField(max_length=500, null=True, blank=True)
    MontantFixe = models.DecimalField(max_digits=10, decimal_places=2)
    Monnaie = models.CharField(max_length=100, null=False,default='CDF')


class Periode(models.Model):
    CodePeriode = models.AutoField(primary_key=True)
    DesignationPeriode = models.CharField(max_length=200, null=False, blank=False)
    Mois = models.IntegerField(default=1)
    Annee = models.IntegerField(default=1960)


class Paiement(models.Model):
    CodePaiement = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CodePeriode = models.ForeignKey(Periode,related_name='list_paiement' ,on_delete=models.CASCADE)
    CodeCotisation = models.ForeignKey(Cotisation,related_name='list_paiement' ,on_delete=models.CASCADE)
    CodePersonnage = models.ForeignKey(Personnage, on_delete=models.CASCADE, related_name='list_paiement')
    MontantPaye = models.DecimalField(max_digits=10, decimal_places=2)
    DatePaiement = models.DateField()
    Observation = models.CharField(max_length=500, null=True, blank=True)
    Monnaie = models.CharField(max_length=100, null=False, default='CDF')

    

