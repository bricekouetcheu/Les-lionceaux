from utilisateurs.models import Utilisateur, Groupe
import django_filters


class UtilisateurFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(field_name="email", lookup_expr="exact")
    username = django_filters.CharFilter(field_name="username", lookup_expr="exact")
    class Meta:
        model = Utilisateur
        fields = []