from django.urls import path, include
from rest_framework import routers
from crecheapp import api
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from . import views
from .myviews import contact

schema_view = get_schema_view(
    openapi.Info(
        title="API Crèche",
        default_version='v1',
        description="Documentation de l'API du projet Crèche",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@creche.fr"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

rooter = routers.DefaultRouter()

rooter.register('blog', api.BlogViewSet, basename='blog')
rooter.register('galerie', api.GalerieViewSet, basename='galerie')
rooter.register('utilisateur', api.UtilisateurViewSet, basename='utilisateur')
rooter.register('parent', api.ParentViewSet, basename='parent')
rooter.register('enfant', api.EnfantViewSet, basename='enfant')

urlpatterns = [
    # path('', views.home, name="home"),
    path('api/', include(rooter.urls)),
    path('api/login', api.loginapi),
    path('api/contact', contact.postcontact),

    # Documentation de l'API
    path('apidoc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
