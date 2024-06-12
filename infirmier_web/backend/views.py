import os
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Personnage,OrdreInfirmier,PersonnageOrdre,CategorieDocument,Document,DocumentPersonnage,Cotisation,Periode,Paiement
from .serializers import PersonnageListSerializer,PersonnageDetailSerializer, OrdreInfirmierListSerializer,OrdreInfirmierDetailSerializer,PersonnageOrdreListSerializer, PersonnageOrdreDetailSerializer, CategorieDocumentListSerializer, CategorieDocumentDetailSerializer, DocumentListSerializer, DocumentDetailSerializer, DocumentPersonnageListSerializer, DocumentPersonnageDetailSerializer, CotisationListSerializer, CotisationDetailSerializer, PeriodeListSerializer, PeriodeDetailSerializer, PaiementListSerializer,PaiementDetailSerializer,PhotoUploadSerializer
from infirmier_web import settings



# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,filters

from django.views.decorators.csrf import csrf_exempt

# For Photo
from django.core.files.storage import default_storage

# Create your views here
class MultipleSerializeMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

class PersonnageViewset(MultipleSerializeMixin,ModelViewSet):
    serializer_class = PersonnageListSerializer
    detail_serializer_class = PersonnageDetailSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('Nom','Postnom','Prenom',)

    queryset = Personnage.objects.all()


class OrdreInfirmierViewset(MultipleSerializeMixin,ModelViewSet):
    serializer_class = OrdreInfirmierListSerializer
    detail_serializer_class = OrdreInfirmierDetailSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('NumeroOrdre',)

    queryset = OrdreInfirmier.objects.all()



class CategorieDocumentViewset(MultipleSerializeMixin,ModelViewSet):
    serializer_class = CategorieDocumentListSerializer
    detail_serializer_class = CategorieDocumentDetailSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('DesignationCategorie',)

    queryset = CategorieDocument.objects.all()


class CotisationViewset(MultipleSerializeMixin,ModelViewSet):
    serializer_class = CotisationListSerializer
    detail_serializer_class = CotisationDetailSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('Libelle',)

    queryset = Cotisation.objects.all()


class PeriodeViewset(MultipleSerializeMixin,ModelViewSet):
    serializer_class = PeriodeListSerializer
    detail_serializer_class = PeriodeDetailSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('DesignationPeriode',)

    queryset = Periode.objects.all()


class DocumentViewset(MultipleSerializeMixin,ModelViewSet):
    serializer_class = DocumentListSerializer
    detail_serializer_class = DocumentDetailSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('Designation',)

    def get_queryset(self):
        queryset = Document.objects.all()
        CodeCategorieDocument = self.request.GET.get('CodeCategorieDocument')
        if CodeCategorieDocument:
            queryset = queryset.filter(CodeCategorieDocument = CodeCategorieDocument)

        return queryset
    

class PersonnageOrdreViewset(MultipleSerializeMixin,ModelViewSet):
    serializer_class =PersonnageOrdreListSerializer
    detail_serializer_class = PersonnageOrdreDetailSerializer
   
    def get_queryset(self):
        queryset = PersonnageOrdre.objects.all()
        CodePersonnage = self.request.GET.get('CodePersonnage')
        CodeOrdre = self.request.GET.get('CodeOrdre')
        if CodePersonnage:
            queryset = queryset.filter(CodePersonnage = CodePersonnage)
        if CodeOrdre:
            queryset = queryset.filter(CodeOrdre = CodeOrdre)
            
        return queryset
    

class DocumentPersonnageViewset(MultipleSerializeMixin,ModelViewSet):
    serializer_class = DocumentPersonnageListSerializer
    detail_serializer_class = DocumentPersonnageDetailSerializer
   
    def get_queryset(self):
        queryset = DocumentPersonnage.objects.all()
        CodeDocument = self.request.GET.get('CodeDocument')
        CodePersonnage = self.request.GET.get('CodePersonnage')
        if CodeDocument:
            queryset = queryset.filter(CodeDocument = CodeDocument)
        if CodePersonnage:
            queryset = queryset.filter(CodePersonnage = CodePersonnage)
            
        return queryset
    

class PaiementViewset(MultipleSerializeMixin,ModelViewSet):
    serializer_class = PaiementListSerializer
    detail_serializer_class = PaiementDetailSerializer
   
    def get_queryset(self):
        queryset = Paiement.objects.all()
        CodePeriode = self.request.GET.get('CodePeriode')
        CodeCotisation = self.request.GET.get('CodeCotisation')
        if CodePeriode:
            queryset = queryset.filter(CodePeriode = CodePeriode)
        if CodeCotisation:
            queryset = queryset.filter(CodeCotisation = CodeCotisation)
            
        return queryset



class PhotoUploadAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PhotoUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            file_name = file.name
            file_path = os.path.join(settings.MEDIA_ROOT, 'Photos', file_name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            photo_url = os.path.join(settings.MEDIA_URL, '', file_name)
            return Response({'PhotoFileName': photo_url}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

