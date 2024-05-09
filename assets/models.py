from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    # Assume company name is unique
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    # Assume User is already created and we are using it here
    # Here we use default User model from Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Device(models.Model):
    # Assume there are only 3 option. If want to add more, add here. 
    # we can use static-configs api for future to avoid hardcoding
    TYPE_CHOICES = [
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('laptop', 'Laptop'),
    ] 
    
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    serial_number = models.CharField(max_length=255, unique=True)
    condition = models.TextField()

    def __str__(self):
        return self.type + ' - ' + self.serial_number

class DeviceAssignment(models.Model):
    # Assume that each device can only be assigned to one employee at a time
    device = models.ForeignKey(Device, related_name='assignments', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='assignments', on_delete=models.CASCADE)
    checked_out = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
    initial_condition = models.TextField()
    return_condition = models.TextField(null=True, blank=True)
