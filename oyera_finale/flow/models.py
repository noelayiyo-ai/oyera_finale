from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.TextField(max_length=15)
    email = models.EmailField(unique=True)

class Vehicle(models.Model):
    number_plate = models.TextField()
    vehicle_type = models.TextField(max_length=20)
    model = models.TextField()
    colour = models.TextField(max_length=25)
    created_at =models.DateTimeField(auto_now_add=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Part(models.Model):
    name = models.CharField(max_length=30)
    decription = models.TextField(max_length=200)
    amount = models.CharField(max_length=20)
    stock_quantity = models.CharField()

class Service(models.Model):
    name = models.CharField(max_length=30)
    labor_estimation = models.CharField()
    description =models.TextField(max_length=200)


class Payment(models.Model):
    amount = models.CharField()
    payment_method = models.CharField(choices=['Cash',''])
    date = models.DateField()
    
