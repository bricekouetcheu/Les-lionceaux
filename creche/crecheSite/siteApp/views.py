from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from . models import Employees
from . serializer import EmployeesSerializer


# def index(request):
# return HttpResponse("Hello, world. You're at the siteApp index.")

class EmployeeList(APIView):

    def get(self, request, *args, **kwargs):
        employees1 = Employees.objects.all()
        serializer = EmployeesSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
