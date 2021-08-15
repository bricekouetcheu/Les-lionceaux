from rest_framework import viewsets
from agenda.serializers import AgendaSerializer
from blog.serializers import BlogSerializer
from agenda.models import Agenda
from blog.models import Blog

from django.http import JsonResponse


class AgendaViewSet(viewsets.ModelViewSet):
    """
    Viewset for Agenda model.
    """

    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()



