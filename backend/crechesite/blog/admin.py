from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class BlogAdmin(admin.ModelAdmin):

    list_display = (
        "titre",
        "image",
        "auteur",
        "status",
        "date_add",
        "date_upd",
    )
    list_filter = (
        "auteur",
        "status",
        "date_add",
        "date_upd",
    )
    search_fields = ("titre",)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Blog, BlogAdmin)