from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'img',
        'slug',
        'titre',
        'auteur',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'auteur',
        'status',
        'date_add',
    )

    def img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="height:80px; width:120px">')
        else:
            return 'Aucun fichier'

    img.short_description = "Prévisualisation"


class GalerieAdmin(admin.ModelAdmin):
    list_display = ('img', 'titre', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
    )

    def img(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="height:80px; width:120px">')
        else:
            return 'Aucun fichier'

    img.short_description = "Prévisualisation"


class UtilisateurAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'adresse',
        'is_directrice',
        'is_accueillante',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'is_directrice',
        'is_accueillante',
        'status',
        'date_add',
    )


class EnfantInLine(admin.TabularInline):
    model = models.Enfant
    extra = 0


class ParentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'localisation',
        'telephone',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'status',
        'date_add',
    )
    inlines = [
        EnfantInLine
    ]


class EnfantAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'prenom',
        'parent',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'parent',
        'status',
        'date_add',
    )

    search_fields = ['nom', 'prenom']


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'email',

        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Blog, BlogAdmin)
_register(models.Galerie, GalerieAdmin)
_register(models.Utilisateur, UtilisateurAdmin)
_register(models.Parent, ParentAdmin)
_register(models.Enfant, EnfantAdmin)
_register(models.Contact, ContactAdmin)