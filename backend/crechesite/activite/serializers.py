from rest_framework import serializers
from activite.models import Activite
from utilisateurs.serializers import GroupeSerializer


class ActiviteSerializer(serializers.ModelSerializer):
    """
    Serializer for Activite model.
    """

    groupe_set = GroupeSerializer()

    class Meta:
        model = Activite
        fields = "__all__"
