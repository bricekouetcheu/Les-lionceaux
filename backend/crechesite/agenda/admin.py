from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AgendaAdmin(admin.ModelAdmin):

    list_display = (
        "date_evenement",
        "heure",
        "titre_evenement",
        "description",
        "visible",
        "date_add",
        "date_upd",
    )
    list_filter = (
        "date_evenement",
        "visible",
        "date_add",
        "date_upd",
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Agenda, AgendaAdmin)