from django.db import models
from flow.models import Client, Service, Part, Payment, Vehicle

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.TextField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    password = models.TextField()
    role =  models.TextField(max_length=30)

class Work(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    part = models.ForeignKey(Part,  on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,  on_delete=models.CASCADE)
    vehicle =models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    status = models.TextField(max_length=20)