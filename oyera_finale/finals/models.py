from django.db import models
from .models import Client, Service, Part, Payment, Vehicle, User

# Create your models here.
class Job(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    part_required = models.ForeignKey(Part,  on_delete=models.CASCADE)
    quantity_required = models.IntegerField()
    unit_cost = models.IntegerField()
    vehicle =models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    problem_description = models.TextField(max_length= 500)
    phone_number = models.CharField(max_length=15)
    total_amount = models.IntegerField()

    def __str__(self):
        return f"{self.client} {self.sevice} {self.part_required} {self.vehicle}"



        
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
   
    

class Vehicle(models.Model):
    number_plate = models.CharField()
    vehicle_type = models.CharField(max_length=20)
    model = models.CharField()
    colour = models.TextField(max_length=25)
    created_at =models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)


class Part(models.Model):
    name = models.CharField(max_length=30)
    decription = models.TextField(max_length=200)
    amount = models.CharField(max_length=20)
    stock_quantity = models.CharField()
    timestamp = models.DateTimeField(auto_created=True)

class Service(models.Model):
    name = models.CharField(max_length=30)
    labor_estimation = models.CharField()
    description =models.TextField(max_length=200)

class Receipt(models.Model):
    amount = models.CharField()
    payment_method = models.CharField(choices=['Cash','Mobile Money','VISA card'])
    date = models.DateField()
    part = models.ForeignKey()
    service = models.ForeignKey()
    Vehicle = models.ForeignKey()



      
