"""
URL configuration for infirmier_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from backend.views import PersonnageViewset,OrdreInfirmierViewset,CategorieDocumentViewset,CotisationViewset,PeriodeViewset,DocumentViewset,PersonnageOrdreViewset,DocumentPersonnageViewset,PaiementViewset,PhotoUploadAPIView

from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()

router.register('personnage',PersonnageViewset,basename='personnage')
router.register('ordre-infirmier',OrdreInfirmierViewset,basename='ordre_infirmier')
router.register('categorie-document',CategorieDocumentViewset,basename='categorie_document')
router.register('cotisation',CotisationViewset,basename='cotisation')
router.register('periode',PeriodeViewset,basename='periode')
router.register('document',DocumentViewset,basename='document')
router.register('personnage-ordre',PersonnageOrdreViewset,basename='personnage_ordre')
router.register('document-personnage',DocumentPersonnageViewset,basename='document_personnage')
router.register('paiement',PaiementViewset,basename='paiement')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/upload/', PhotoUploadAPIView.as_view(), name='photo_upload'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
