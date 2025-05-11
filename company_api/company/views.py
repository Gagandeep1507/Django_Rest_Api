from django.shortcuts import render 
from rest_framework import viewsets , status
from .models import Company , Employee
from .serialisers import CompanySerializer , EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #company/{companyid}/employee
    @action(detail = True, methods = ['GET'])
    def employee(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found'},status=status.HTTP_404_NOT_FOUND)
        
        emply = Employee.objects.filter(company=company)

        if not emply.exists():
            return Response({'message' : 'This Employee is not find'} , status=status.HTTP_404_NOT_FOUND )
        emply_ser = EmployeeSerializer(emply, many= True)
        return Response(emply_ser.data)


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer