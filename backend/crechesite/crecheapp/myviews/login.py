from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import json
from crecheapp import models
from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi
from rest_framework.decorators import api_view
from crecheapp.schemaperso import login_schema
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Token
from rest_framework.authtoken.models import Token


@csrf_exempt
@swagger_auto_schema(method='post', manual_parameters=login_schema)
@api_view(['POST'])
def loginapi(request):
    status, message, datas, token = False, "", "", ""

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
                    cle, created = Token.objects.get_or_create(user=utilisateur)
                    try:
                        profile = models.Utilisateur.objects.filter(user=utilisateur).values('id', 'user__username',
                                                                                             'user__email',
                                                                                             'is_directrice',
                                                                                             'is_accueillante').first()
                        if profile:
                            status = True
                            datas = profile
                            message = "Connexion réussite."
                        else:
                            message = "Cet utilisateur n'est pas enregistré."
                    except Exception as e:
                        print(e)
                    try:
                        profile = models.Parent.objects.filter(user=utilisateur).values('id', 'user__username',
                                                                                        'user__email', 'localisation',
                                                                                        'telephone',
                                                                                        'parent_enfant__nom',
                                                                                        'parent_enfant__prenom').first()
                        if profile:
                            status = True
                            datas = profile
                            message = "Connexion réussite."
                    except Exception as e:
                        print(e)

                    token = cle.key
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
        'token': token,
    }
    return JsonResponse(data, safe=False)