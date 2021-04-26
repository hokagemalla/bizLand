from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import EmployeeSerialiser

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def port(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')

@api_view(['GET',])
def getEmployee(request,pk):
    employee1 = Employees.objects.get(pk = pk)
    serializer = EmployeeSerialiser(employee1)
    return Response(serializer.data)

@api_view(['POST',])
def postEmployee(request):
    emp_data = request.data

    new_employee = Employees(firstname=emp_data['firstname'], lastname=emp_data['lastname'], emp_id=emp_data['emp_id'])
    new_employee.save()

    serializer = EmployeeSerialiser(new_employee)

    return Response(serializer.data)

@api_view(['PUT',])
def updateEmployee(request,pk):
    employee1 = Employees.objects.get(pk = pk)
    serializer = EmployeeSerialiser(employee1,request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "update successful"
        return Response(data= data)

    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def deleteEmployee(request,pk):
    employee1 = Employees.objects.get(pk = pk)
    operation = employee1.delete()
    data = {}
    if operation:
        data["success"] = "delete successful"
        return Response(data= data)


class EmployeeList(APIView):

    def get(self,request):
        employee1 = Employees.objects.all()
        serializer = EmployeeSerialiser(employee1,many=True)
        return Response(serializer.data)

    def post(self,request):
        emp_data = request.data

        new_employee = Employees(firstname=emp_data['firstname'],lastname=emp_data['lastname'],emp_id=emp_data['emp_id'])
        new_employee.save()

        serializer = EmployeeSerialiser(new_employee)

        return Response(serializer.data)
