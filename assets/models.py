from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)


class Device(models.Model):
    TYPE_CHOICES = [
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('laptop', 'Laptop'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    serial_number = models.CharField(max_length=255, unique=True)
    condition = models.TextField()

class DeviceAssignment(models.Model):
    device = models.ForeignKey(Device, related_name='assignments', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='assignments', on_delete=models.CASCADE)
    checked_out = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
    initial_condition = models.TextField()
    return_condition = models.TextField(null=True, blank=True)
