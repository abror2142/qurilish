from django.shortcuts import render
from rest_framework import viewsets
from .models import Qurilish, QurilishTashkiloti, Hudud
from .serializers import QurilishSerializer, QurilishTashkilotiSerializer, HududSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions


class HududAPIView(viewsets.ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class QurilishTashkilotiAPIView(viewsets.ModelViewSet):
    queryset = QurilishTashkiloti.objects.all()
    serializer_class = QurilishTashkilotiSerializer
    permission_classes = [DjangoModelPermissions]
    

class QurilishAPIView(viewsets.ModelViewSet):
    queryset = Qurilish.objects.all()
    serializer_class = QurilishSerializer
    permission_classes = [DjangoModelPermissions]
    