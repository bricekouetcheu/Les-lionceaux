
from django.db import models
from utilisateurs.models import Groupe

class Activite(models.Model):
    """Model definition for Activite."""

    ART = (("danse", "Danse"), ("chant", "Chant"), ("desin", "Desin"))
    LECTURE = (("pichou", "Pichou"), ("dingo", "Dingo"))
    # TODO: Define fields here
    date_activite = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    groupe_set = models.ManyToManyField(Groupe, related_name="activitygroup")
    art = models.CharField(max_length=20, choices=ART)
    lecture = models.CharField(max_length=20, choices=LECTURE)
    remarque = models.TextField()

    class Meta:
        """Meta definition for Activite."""

        verbose_name = "Activité"
        verbose_name_plural = "Activités"

    def __str__(self):
        """Unicode representation of Activite."""
        return f"activité du {self.date_activite}"