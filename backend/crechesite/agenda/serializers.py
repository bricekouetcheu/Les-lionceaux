from rest_framework import serializers
from agenda.models import Agenda


class AgendaSerializer(serializers.ModelSerializer):
    """
    Serializer for Agenda model.
    """

    class Meta:
        model = Agenda
        fields = "__all__"