from django.db import models
from django.contrib.auth.models import User
# from django.utils.text import slugify
from autoslug import AutoSlugField


# Create your models here.

class Blog(models.Model):
    """Model definition for Blog."""
    # TODO: Define fields here
    titre = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='titre', unique=True, null=True, blank=True)
    description = models.TextField()
    image = models.FileField(upload_to="blog/image")
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='auteur_article', null=True, blank=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Blog."""

        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        """Unicode representation of Blog."""
        return self.titre


class Galerie(models.Model):
    """Model definition for Galerie."""
    titre = models.CharField(max_length=250)
    image = models.FileField(upload_to="galerie/image", default="blog-1.jpg")

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Galerie."""

        verbose_name = 'Galerie'
        verbose_name_plural = 'Galeries'

    def __str__(self):
        """Unicode representation of Galerie."""
        return self.titre


class Utilisateur(models.Model):
    """Model definition for Utilisateur."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='administration')
    adresse = models.CharField(max_length=250)
    is_directrice = models.BooleanField()
    is_accueillante = models.BooleanField()

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Utilisateur."""

        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        """Unicode representation of Utilisateur."""
        return self.user.username


class Parent(models.Model):
    """Model definition for Parent."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parent')
    localisation = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Parent."""

        verbose_name = 'Parent'
        verbose_name_plural = 'Parents'

    def __str__(self):
        """Unicode representation of Parent."""
        return self.user.username


class Enfant(models.Model):
    """Model definition for Enfant."""
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enfant')
    nom = models.CharField(max_length=250, null=True, blank=True)
    prenom = models.CharField(max_length=250, null=True, blank=True)

    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='parent_enfant')

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Enfant."""

        verbose_name = 'Enfant'
        verbose_name_plural = 'Enfants'

    def __str__(self):
        """Unicode representation of Enfant."""
        return self.nom


class Contact(models.Model):
    """Model definition for Contact."""

    nom = models.CharField(max_length=254)
    prenom = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=254, null=True)
    message = models.TextField()

    status = models.BooleanField(default=True)
    date_add = models.DateField(auto_now_add=True)
    date_upd = models.DateField(auto_now=True)

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.nom