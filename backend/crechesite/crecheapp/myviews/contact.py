from django.shortcuts import render
from crecheapp import models
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
import re

from drf_yasg2.utils import swagger_auto_schema
from drf_yasg2 import openapi
from rest_framework.decorators import api_view
from crecheapp.schemaperso import contact_schema


def validate_contact(contact):
    regex = re.compile("^(\+[ ]?)?((\d){1,2}[ ]?){8,}$")
    status = regex.match(contact.strip())
    if status:
        return True
    else:
        return False


@csrf_exempt
@swagger_auto_schema(method='post', manual_parameters=contact_schema)
@api_view(['POST'])
def postcontact(request):
    success, message = False, ""

    if request.method == "POST":
        try:
            try:
                postdata = json.loads(request.body.decode('utf-8'))
                email = postdata['email']
                nom = postdata['nom']
                prenom = postdata['prenom']
                text = postdata['message']
                tel = postdata['telephone']
            except:
                email = request.POST.get("email")
                nom = request.POST.get("nom")
                prenom = request.POST.get("prenom")
                text = request.POST.get("message")
                tel = request.POST.get("telephone")

            if nom != '' and not nom.isspace() and prenom != '' and not prenom.isspace() and text != '' and not text.isspace() and email != '' and validate_contact(
                    tel):
                try:
                    validate_email(email)
                    contact = models.Contact()
                    contact.email = email
                    contact.nom = nom
                    contact.prenom = prenom
                    contact.message = text
                    contact.telephone = tel
                    contact.save()
                    success = True
                    message = "Merci, votre message a été envoyé, nous vous répondrons dans un bref délai."
                except Exception as e:
                    print("bad email, details:", e)
                    message = "Merci de renseigner un email correct"

            else:
                message = "Remplie correctement les champs."
        except:
            message = "Une erreur s'est produite contacter le webmaster."
    else:
        message = "Erreur de Requête"

    data = {
        'status': success,
        'message': message,
    }
    return JsonResponse(data, safe=False)
