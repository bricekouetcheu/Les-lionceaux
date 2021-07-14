# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Utilisateur(AbstractUser):
    """Model definition for Utilisateur."""

    localisation = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)
    is_directrice = models.BooleanField(default=True)
    is_accueillante = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Utilisateur."""

        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        """Unicode representation of Utilisateur."""
        return self.first_name


class Groupe(models.Model):
    """Model definition for Groupe."""

    nom = models.CharField(max_length=250)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Groupe."""

        verbose_name = "Groupe"
        verbose_name_plural = "Groupes"

    def __str__(self):
        """Unicode representation of Groupe."""
        return self.nom


class Enfant(models.Model):
    """Model definition for Enfant."""

    nom = models.CharField(max_length=250, null=True, blank=True)
    prenom = models.CharField(max_length=250, null=True, blank=True)

    parent = models.ForeignKey(
        Utilisateur, on_delete=models.CASCADE, related_name="parent_enfant"
    )
    groupe = models.ForeignKey(
        Groupe,
        on_delete=models.CASCADE,
        related_name="groupe_enfant",
        blank=True,
        null=True,
    )

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Enfant."""

        verbose_name = "Enfant"
        verbose_name_plural = "Enfants"

    def __str__(self):
        """Unicode representation of Enfant."""
        return self.nom