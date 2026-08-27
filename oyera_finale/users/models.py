from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Client(AbstractUser):
    ROLE ={
        ('client','client')
    }


class Staff(AbstractUser):
    ROLE ={
        ('admin','admin'),
        ('senior_technician', 'senior_technician'),
        ('junior_technician', 'junior_technician'),
    }