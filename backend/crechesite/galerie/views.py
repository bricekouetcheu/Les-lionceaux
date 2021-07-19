from rest_framework import viewsets
from galerie.serializers import GalerieSerializer, AlbumSerializer
from galerie.models import Galerie, Album


class GalerieViewSet(viewsets.ModelViewSet):
    """
    Viewset for Galerie model.
    """

    serializer_class = GalerieSerializer
    queryset = Galerie.objects.all()


class AlbumViewSet(viewsets.ModelViewSet):
    """
    Viewset for Album model.
    """

    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
