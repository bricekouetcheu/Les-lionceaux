from rest_framework import serializers
from activite.models import Activite
from utilisateurs.serializers import GroupeSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class ActiviteSerializer(WritableNestedModelSerializer):
    """
    Serializer for Activite model.
    """

    groupe_set = GroupeSerializer(many=True)

    class Meta:
        model = Activite
        fields = "__all__"