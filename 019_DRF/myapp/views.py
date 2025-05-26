from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from myapp.serializer import *

# Create your views here.
@api_view(['GET'])
def index(request):
    allStudents = Student.objects.all()
    ser = StudentSerializer(allStudents,many=True)
    return Response({"students":ser.data})

@api_view(['POST'])
def add(request):
    try :
        ser =  StudentSerializer(data= request.data)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"something went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data inserted successfully"})
    except Exception as e:
        print(e)
        return Response({"error":e,"message":"something went wrong"})


@api_view(['PUT'])
def update(request,id):
    try:
        student = Student.objects.get(pk=id)
        ser = StudentSerializer(student,request.data,partial=True)
        if not ser.is_valid():
            return Response({"errors":ser.errors,"message":"something went wrong"})
        else:
            ser.save()
            return Response({"data":ser.data,"message":"Data updated successfully"})
    except Exception as e:
        return Response({"error":e,"message":"something went wrong"})

@api_view(["DELETE"])
def delete(request,id):

    try:
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({"success":True})
    except Exception as e:
         return Response({"error":e,"message":"something went wrong"})
    