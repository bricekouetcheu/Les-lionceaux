from rest_framework import viewsets
from utilisateurs.serializers import (
    UtilisateurSerializer,
    GroupeSerializer,
    EnfantSerializer,
)
from drf_multiple_model.views import ObjectMultipleModelAPIView
from utilisateurs.models import Utilisateur, Groupe, Enfant
from rest_framework import filters
from django.http import JsonResponse
from utilisateurs.filters import UtilisateurFilter


class UtilisateurViewSet(viewsets.ModelViewSet):
    """
    Viewset for Utilisateur model.
    """

    serializer_class = UtilisateurSerializer
    queryset = Utilisateur.objects.all()
    filterset_class = UtilisateurFilter


class GroupeViewSet(viewsets.ModelViewSet):
    """
    Viewset for Groupe model.
    """

    serializer_class = GroupeSerializer
    queryset = Groupe.objects.all()


class EnfantViewSet(viewsets.ModelViewSet):
    """
    Viewset for Enfant model.
    """

    serializer_class = EnfantSerializer
    queryset = Enfant.objects.all()