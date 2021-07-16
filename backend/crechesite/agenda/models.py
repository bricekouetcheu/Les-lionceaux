from django.db import models
from utilisateurs.models import Groupe

# Create your models here.


class Agenda(models.Model):
    """Model definition for Agenda."""

    # TODO: Define fields here
    date_evenement = models.DateField()
    heure = models.TimeField()
    titre_evenement = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    groupe = models.ManyToManyField(Groupe, related_name="agenda_groupe")
    visible = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Agenda."""

        app_label = "agenda"
        verbose_name = "Agenda"
        verbose_name_plural = "Agenda"

    def __str__(self):
        """Unicode representation of Agenda."""
        return self.titre_evenement