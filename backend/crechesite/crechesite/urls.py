from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from activite.views import ActiviteViewSet
from agenda.views import AgendaViewSet
from blog.views import BlogViewSet
from galerie.views import GalerieViewSet, AlbumViewSet
from utilisateurs.views import UtilisateurViewSet, GroupeViewSet, EnfantViewSet

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

"""
Mise en place des routers de l'application Common
"""
rooter = routers.DefaultRouter()
# rooter.register("", SearchAPIView, basename="search")
rooter.register("activite", ActiviteViewSet, basename="activite")
rooter.register("agenda", AgendaViewSet, basename="agenda")
rooter.register("blog", BlogViewSet, basename="blog")
rooter.register("galerie", GalerieViewSet, basename="galerie")
rooter.register("album", AlbumViewSet, basename="album")
rooter.register("utilisateur", UtilisateurViewSet, basename="utilisateur")
rooter.register("groupe", GroupeViewSet, basename="groupe")
rooter.register("enfant", EnfantViewSet, basename="enfant")

schema_view = get_schema_view(
    openapi.Info(
        title="Lionceaux API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(rooter.urls)),
    #path("search", view),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    # doc
     path(
         "swagger(?P<format>\.json|\.yaml)",
         schema_view.without_ui(cache_timeout=0),
         name="schema-json",
     ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
         name="schema-swagger-ui",
     ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)