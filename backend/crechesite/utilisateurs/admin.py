# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class UtilisateurAdmin(UserAdmin):

    list_display = (
        "first_name",
        "last_name",
        "email",
        "localisation",
        "telephone",
        "adresse",
        "is_directrice",
        "is_accueillante",
        "is_parent",
    )
    list_filter = (
        "is_directrice",
        "is_accueillante",
        "is_parent",
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "localisation",
                    "telephone",
                    "is_directrice",
                    "is_accueillante",
                    "is_parent",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "localisation",
                    "telephone",
                    "is_directrice",
                    "is_accueillante",
                    "is_parent",
                )
            },
        ),
    )

    search_fields = ("email", "last_name", "first_name")
    ordering = ("last_name",)


class GroupeAdmin(admin.ModelAdmin):

    list_display = ("nom", "status", "date_add", "date_upd")
    list_filter = (
        "status",
        "date_add",
        "date_upd",
    )


class EnfantAdmin(admin.ModelAdmin):

    list_display = (
        "nom",
        "prenom",
        "parent",
        "groupe",
        "status",
        "date_add",
        "date_upd",
    )
    list_filter = (
        "parent",
        "groupe",
        "status",
        "date_add",
        "date_upd",
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Utilisateur, UtilisateurAdmin)
_register(models.Groupe, GroupeAdmin)
_register(models.Enfant, EnfantAdmin)

