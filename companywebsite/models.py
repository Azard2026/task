from django.db import models

# Create your models here.
class contact(models.Model):
    uname=models.CharField(max_length=60)
    email=models.EmailField(max_length=130)
    address=models.TextField()
    phone=models.CharField(max_length=12)
    datetime=models.CharField(max_length=120)
    message=models.TextField()