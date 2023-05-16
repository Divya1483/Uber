from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=18 , null=True , blank=True)
    last_name  = models.CharField(max_length=15 , null=True , blank=True)
    date_of_birth = models.DateField(max_length=8 , null=True , blank=True)
    mobile_number = models.IntegerField(max_length=10 , null=True , blank=True)

    GENDER_TYPES = (
        (1,'Male'),
        (2,'Female'),
        (3,'Other'),
    )
    gender_types = models.IntegerField(
        choices =  GENDER_TYPES
    
    )

class Orders(models.Model):
    order_name = models.CharField(max_length=15 ,null=True , blank=True)
    order_price = models.IntegerField(max_length=15 ,null=True , blank=True)
    order_discount = models.IntegerField(max_length=5 ,null=True , blank=True)
    order_quantity = models.IntegerField(max_length=100 ,null=True , blank=True)
    order_address = models.TextField(max_length=100 ,null=True , blank=True)
    order_place_at = models.DateTimeField(max_length=100 ,null=True , blank=True)

