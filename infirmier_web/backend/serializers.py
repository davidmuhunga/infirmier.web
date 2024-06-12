from rest_framework import serializers
from .models import (
    Personnage, 
    OrdreInfirmier, 
    PersonnageOrdre, 
    CategorieDocument, 
    Document, 
    DocumentPersonnage, 
    Cotisation, 
    Periode, 
    Paiement
)

class PersonnageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnage
        fields = ['CodePersonnage','Nom','Postnom','Prenom','DateNaissance','PhotoFileName']


class PersonnageOrdreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonnageOrdre
        fields = ['CodePersonnageOrdre','CodePersonnage','CodeOrdre','Active','RaisonDesactivation','DateDesactivation']
        

class DocumentPersonnageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentPersonnage
        fields = ['CodeDocumentPersonnage','CodeDocument','CodePersonnage','DateObtention','Valide','Url','DateEnreg']


class OrdreInfirmierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdreInfirmier
        fields = ['CodeOrdre','NumeroOrdre','DateObtention']


class CategorieDocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieDocument
        fields = ['CodeCategorieDocument','DesignationCategorie']


class DocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['CodeDocument','CodeCategorieDocument','Designation']


class CotisationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotisation
        fields = ['CodeCotisation','Libelle','Observation','MontantFixe','Monnaie']

class PeriodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periode
        fields = ['CodePeriode','DesignationPeriode','Mois','Annee']

class PaiementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = ['CodePaiement','CodePeriode','CodeCotisation','CodePersonnage','MontantPaye','DatePaiement','Monnaie','Observation']


class PersonnageDetailSerializer(serializers.ModelSerializer):

    list_personnage_ordre = PersonnageOrdreListSerializer(many=True)
    list_document_personnage = DocumentPersonnageListSerializer(many=True)
    list_paiement = PaiementListSerializer(many=True)

    class Meta:
        model = Personnage
        fields = ['CodePersonnage','Nom','Postnom','Prenom','DateNaissance','PhotoFileName','list_personnage_ordre','list_document_personnage','list_paiement']


class DocumentDetailSerializer(serializers.ModelSerializer):
    list_document_personnage = DocumentPersonnageListSerializer(many=True)

    class Meta:
        model = Document
        fields = ['CodeDocument','CodeCategorieDocument','Designation','list_document_personnage']


class PersonnageOrdreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonnageOrdre
        fields = ['CodePersonnage','CodeOrdre','Active','RaisonDesactivation','DateDesactivation']


class DocumentPersonnageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentPersonnage
        fields = ['CodeDocument','CodePersonnage','DateObtention','Valide','Url','DateEnreg']


class OrdreInfirmierDetailSerializer(serializers.ModelSerializer):
    list_personnage_ordre = PersonnageOrdreListSerializer(many=True)

    class Meta:
        model = OrdreInfirmier
        fields = ['CodeOrdre','NumeroOrdre','DateObtention','list_personnage_ordre']


class CategorieDocumentDetailSerializer(serializers.ModelSerializer):
    list_documents = DocumentListSerializer(many=True)

    class Meta:
        model = CategorieDocument
        fields = ['CodeCategorieDocument','DesignationCategorie','list_documents']

class CotisationDetailSerializer(serializers.ModelSerializer):
    list_paiement = PaiementListSerializer(many=True)

    class Meta:
        model = Cotisation
        fields = ['CodeCotisation','Libelle','Observation','MontantFixe','list_paiement']


class PeriodeDetailSerializer(serializers.ModelSerializer):
    list_paiement = PaiementListSerializer(many=True)

    class Meta:
        model = Periode
        fields = ['CodePeriode','DesignationPeriode','list_paiement']

class PaiementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = ['CodePaiement','CodePeriode','CodeCotisation','CodePersonnage','MontantPaye','DatePaiement','Observation']


class PhotoUploadSerializer(serializers.Serializer):
    file = serializers.ImageField()