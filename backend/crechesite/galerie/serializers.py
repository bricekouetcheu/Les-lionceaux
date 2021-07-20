from rest_framework import serializers
from galerie.models import Album, Galerie


class GalerieSerializer(serializers.ModelSerializer):
    """
    Serializer for Galerie model.
    """

    class Meta:
        model = Galerie
        fields = "__all__"
        # read_only_fields = ("album",)


class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for Album model.
    """

    album_galerie = GalerieSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = "__all__"
