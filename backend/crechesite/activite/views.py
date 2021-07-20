from rest_framework import viewsets
from activite.serializers import ActiviteSerializer
from activite.models import Activite
from rest_framework.permissions import IsAuthenticated


class ActiviteViewSet(viewsets.ModelViewSet):
    """
    Viewset for Activite model.
    """

    # permission_classes = (IsAuthenticated,)

    serializer_class = ActiviteSerializer
    queryset = Activite.objects.all()