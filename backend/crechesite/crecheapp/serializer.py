from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'id': {'read_only': True}}
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        )


class BlogSerializer(serializers.ModelSerializer):
    auteur_article = UserSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = models.Blog
        fields = "__all__"
        depth = 1


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = "__all__"


class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Groupe
        fields = "__all__"


class GalerieSerializer(serializers.ModelSerializer):
    album_galerie = AlbumSerializer(many=True, required=False)

    class Meta:
        model = models.Galerie
        fields = "__all__"
        depth = 1


class UtilisateurSerializer(serializers.ModelSerializer):
    administration = UserSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = models.Utilisateur
        fields = "__all__"
        depth = 1


class ParentSerializer(serializers.ModelSerializer):
    parent = UserSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = models.Parent
        fields = "__all__"
        depth = 1


class EnfantSerializer(serializers.ModelSerializer):
    groupe_enfant = GroupeSerializer(many=True, required=False)
    parent_enfant = ParentSerializer(many=True, required=False)

    class Meta:
        model = models.Enfant
        fields = "__all__"
        depth = 2


class EnfantSerializer(serializers.ModelSerializer):
    groupe_enfant = GroupeSerializer(many=True, required=False)
    parent_enfant = ParentSerializer(many=True, required=False)

    class Meta:
        model = models.Enfant
        fields = "__all__"
        depth = 2