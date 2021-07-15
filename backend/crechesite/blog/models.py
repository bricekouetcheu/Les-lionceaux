from django.db import models
from autoslug import AutoSlugField
from utilisateurs.models import Utilisateur

# Create your models here.


class Blog(models.Model):
    """Model definition for Blog."""

    # TODO: Define fields here
    titre = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from="titre", unique=True, null=True, blank=True)
    description = models.TextField()
    image = models.FileField(upload_to="blog/image", default="blog-1.jpg")
    auteur = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name="auteur_article",
        null=True,
        blank=True,
    )

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Blog."""

        app_label = "blog"
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        """Unicode representation of Blog."""
        return self.titre
