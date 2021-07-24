from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AlbumAdmin(admin.ModelAdmin):

    list_display = ("titre", "slug", "status", "date_add", "date_upd")
    list_filter = (
        "status",
        "date_add",
        "date_upd",
    )
    search_fields = ("slug",)


class GalerieAdmin(admin.ModelAdmin):

    list_display = (
        "album",
        "titre",
        "image",
        "status",
        "date_add",
        "date_upd",
    )
    list_filter = (
        "album",
        "status",
        "date_add",
        "date_upd",
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Album, AlbumAdmin)
_register(models.Galerie, GalerieAdmin)
