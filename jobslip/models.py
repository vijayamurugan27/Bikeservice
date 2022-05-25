from email.policy import default
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.

class Customer(models.Model):
    MY_CHOICE=[
        ('Royal enfield','Royal enfield'),
        ('KTM','KTM'),
        ('Yamaha','Yamaha'),
        ('TVS','TVS'),
        ('Bajaj','Bajaj'),
        ('Honda','Honda'),
    ]
    MY_WARRANTY=(
        ('Yes','Yes'),
        ('Nil','Nil'),
    )
    jno=models.AutoField(primary_key=True)
    date=models.DateField(auto_now_add=True)
    name=models.CharField(max_length=30)
    brand=models.CharField(max_length=50,choices=MY_CHOICE)
    model=models.CharField(max_length=10)
    complaint=models.TextField(blank=True)
    warranty=models.CharField(max_length=50,choices=MY_WARRANTY)
    email=models.EmailField()
    contact= models.IntegerField(blank=True)
    address=models.CharField(max_length=100)

    class Meta:
        db_table = 'Customer'
