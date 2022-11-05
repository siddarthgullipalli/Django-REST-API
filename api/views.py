from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Doctor

from .serializers import Doctorserializer 

# Create your views here.

@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'GETALL' : '/getall/',
        'GET': '/get/<str:pk>/',
        'POST':'/post/',
        'PUT' : '/PUT/<str:pk>/',
        'DELETE':'/delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def Doctors(request):
    doctors = Doctor.objects.all()
    serializer = Doctorserializer(doctors , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def doctor(request , pk):
    doctor = Doctor.objects.get(id = pk)
    serializer = Doctorserializer(doctor , many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Adddoctor(request):
    serializer = Doctorserializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Editdoctor(request , pk):
    doctor = Doctor.objects.get(id = pk)
    serializer = Doctorserializer(instance =doctor ,   data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deletedoctor(request , pk):
    doctor = Doctor.objects.get(id = pk)
    doctor.delete()
    return Response("sucessfully deleted")


    
