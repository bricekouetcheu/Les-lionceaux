from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Album(models.Model):
    """Model definition for Galerie."""

    titre = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from="titre", unique=True, null=True, blank=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Galerie."""

        app_label = "galerie"
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        """Unicode representation of Galerie."""
        return self.titre


class Galerie(models.Model):
    """Model definition for Galerie."""

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="album_galerie",
        blank=True,
        null=True,
    )
    titre = models.CharField(max_length=250, blank=True, null=True)
    image = models.FileField(upload_to="galerie/image", default="blog-1.jpg")

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Galerie."""

        app_label = "galerie"
        verbose_name = "Galerie"
        verbose_name_plural = "Galeries"

    def __str__(self):
        """Unicode representation of Galerie."""
        return self.titre
