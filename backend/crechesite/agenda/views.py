from rest_framework import viewsets
from agenda.serializers import AgendaSerializer
from blog.serializers import BlogSerializer
from agenda.models import Agenda
from blog.models import Blog
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework import filters
from django.http import JsonResponse


class AgendaViewSet(viewsets.ModelViewSet):
    """
    Viewset for Agenda model.
    """

    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()


def view(request):
    query = request.GET.get("query", None)
    b = Blog.objects.all()
    a = Agenda.objects.all()

    if query:
        b = Blog.objects.filter(titre__icontains=query)
        a = Agenda.objects.filter(titre_evenement__icontains=query)

    return JsonResponse(
        {
            "b": BlogSerializer(instances=b, many=True).data,
            "a": AgendaSerializer(instances=a, many=True).data,
        }
    )