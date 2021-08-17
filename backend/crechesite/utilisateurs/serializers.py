from rest_framework import serializers
from utilisateurs.models import Utilisateur, Groupe, Enfant


class UtilisateurSerializer(serializers.ModelSerializer):
    """
    Serializer for Utilisateur model.
    """

    class Meta:
        model = Utilisateur
        fields = "__all__"


class GroupeSerializer(serializers.ModelSerializer):
    """
    Serializer for Groupe model.
    """

    class Meta:
        model = Groupe
        fields = "__all__"


class EnfantSerializer(serializers.ModelSerializer):
    """
    Serializer for Enfant model.
    """

    class Meta:
        model = Enfant
        fields = "__all__"