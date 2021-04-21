from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from . import serializer, models
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import json

from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi
from rest_framework.decorators import api_view
from crecheapp.schemaperso import login_schema


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.BlogSerializer
    queryset = models.Blog.objects.filter(status=True)

class GalerieViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.GalerieSerializer
    queryset = models.Galerie.objects.filter(status=True)

class UtilisateurViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UtilisateurSerializer
    queryset = models.Utilisateur.objects.filter(status=True)

class ParentViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ParentSerializer
    queryset = models.Parent.objects.filter(status=True)

class EnfantViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.EnfantSerializer
    queryset = models.Enfant.objects.filter(status=True)



@csrf_exempt
@swagger_auto_schema(method='post', manual_parameters=login_schema)
@api_view(['POST'])
def loginapi(request):
    status, message, datas = False, "", ""


    if request.method == "POST":
        try:
            postdata = json.loads(request.body.decode('utf-8'))
            username = postdata['username']
            password = postdata['password']
        except:
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

        utilisateur = User.objects.filter(Q(email=username) | Q(username=username)).first()
        if utilisateur:
            if utilisateur.is_active:
                user = authenticate(username=utilisateur.username, password=password)
                if user is not None:
                    try:
                        profile = models.Utilisateur.objects.filter(user=utilisateur).values('id', 'user__username', 'user__email', 'is_directrice','is_accueillante').first()
                        if profile:
                            status = True
                            datas = profile
                            message = "Connexion réussite."
                    except Exception as e:
                        print(e)
                    try:
                        profile = models.Parent.objects.filter(user=utilisateur).values('id', 'user__username', 'user__email', 'localisation', 'telephone', 'enfant_nom', 'enfant_prenom').first()
                        if profile:
                            status = True
                            datas = profile
                            message = "Connexion réussite."
                    except Exception as e:
                        print(e)
                else:
                    message = "Vos identifiants ne sont pas correctes."
            else:
                message = "Votre compte est désactivé."
        else:
            message = "Vos identifiants n\'existent pas "
    data = {
        'success': status,
        'message': message,
        'user': datas,
    }
    return JsonResponse(data, safe=False)