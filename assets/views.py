from rest_framework import viewsets
from .models import Device, DeviceAssignment, Employee, Company
from .serializers import DeviceSerializer, AssignmentSerializer, EmployeeSerializer, CompanySerializer

class DeviceViewSet(viewsets.ModelViewSet):
    # By default, this will allow GET, POST, PUT, DELETE
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    # By default, this will allow GET, POST, PUT, DELETE
    queryset = DeviceAssignment.objects.all()
    serializer_class = AssignmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    # By default, this will allow GET, POST, PUT, DELETE
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    # By default, this will allow GET, POST, PUT, DELETE
    queryset = Company.objects.all()
    serializer_class = CompanySerializer