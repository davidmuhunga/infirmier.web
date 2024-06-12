from django.contrib import admin

# Register your models here.

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

#@admin.register(Personnage)
class PersonnageAdmin(admin.ModelAdmin):
    list_display = ('CodePersonnage', 'Nom', 'Postnom', 'Prenom', 'DateNaissance', 'PhotoFileName')
    search_fields = ('Nom', 'Postnom', 'Prenom')

@admin.register(OrdreInfirmier)
class OrdreInfirmierAdmin(admin.ModelAdmin):
    list_display = ('CodeOrdre', 'NumeroOrdre', 'DateObtention')
    search_fields = ('NumeroOrdre',)

@admin.register(PersonnageOrdre)
class PersonnageOrdreAdmin(admin.ModelAdmin):
    list_display = ('CodePersonnage', 'CodeOrdre', 'Active', 'RaisonDesactivation', 'DateDesactivation')
    search_fields = ('CodePersonnage__Nom', 'CodeOrdre__NumeroOrdre')
    list_filter = ('Active',)

@admin.register(CategorieDocument)
class CategorieDocumentAdmin(admin.ModelAdmin):
    list_display = ('CodeCategorieDocument', 'DesignationCategorie')
    search_fields = ('DesignationCategorie',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('CodeDocument', 'CodeCategorieDocument', 'Designation')
    search_fields = ('Designation', 'CodeCategorieDocument__DesignationCategorie')

@admin.register(DocumentPersonnage)
class DocumentPersonnageAdmin(admin.ModelAdmin):
    list_display = ('CodeDocument', 'CodePersonnage', 'DateObtention', 'Valide', 'Url', 'DateEnreg')
    search_fields = ('CodeDocument__Designation', 'CodePersonnage__Nom')
    list_filter = ('Valide',)

@admin.register(Cotisation)
class CotisationAdmin(admin.ModelAdmin):
    list_display = ('CodeCotisation', 'Libelle', 'Observation', 'MontantFixe')
    search_fields = ('Libelle',)

@admin.register(Periode)
class PeriodeAdmin(admin.ModelAdmin):
    list_display = ('CodePeriode', 'DesignationPeriode')
    search_fields = ('DesignationPeriode',)

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('CodePaiement', 'CodePeriode', 'CodeCotisation', 'CodePersonnage', 'MontantPaye', 'DatePaiement', 'Observation')
    search_fields = ('CodePeriode__DesignationPeriode', 'CodeCotisation__Libelle', 'CodePersonnage__Nom')
    list_filter = ('DatePaiement',)


admin.site.register(Personnage,PersonnageAdmin)


