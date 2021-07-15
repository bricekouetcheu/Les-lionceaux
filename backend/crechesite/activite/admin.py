from django.contrib import admin

from . import models


class ActiviteAdmin(admin.ModelAdmin):

    list_display = (
        "date_activite",
        "heure_debut",
        "heure_fin",
        "art",
        "lecture",
    )
    list_filter = (
        "date_activite",
        "id",
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Activite, ActiviteAdmin)