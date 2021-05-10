from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from . import serializer, models
from django.db.models import Q, Count


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.BlogSerializer
    queryset = models.Blog.objects.filter(status=True)


class GaleriesViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.GalerieSerializer
    queryset = models.Galerie.objects.filter(status=True)


class GalerieViewSet(generics.ListAPIView):
    serializer_class = serializer.GalerieSerializer
    queryset = models.Galerie.objects.filter(status=True)

    def list(self, request, slug):
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(album__id=int(slug)))
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class UtilisateurViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UtilisateurSerializer
    queryset = models.Utilisateur.objects.filter(status=True)


class ParentViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ParentSerializer
    queryset = models.Parent.objects.filter(status=True)


class EnfantViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.EnfantSerializer
    queryset = models.Enfant.objects.filter(status=True)


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.AlbumSerializer
    queryset = models.Album.objects.filter(status=True)


class GroupeViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.GroupeSerializer
    queryset = models.Groupe.objects.filter(status=True)