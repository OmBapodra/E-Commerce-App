from django.db import models

# Create your models here.
class UserModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    contact=models.IntegerField(default=0)
    password=models.CharField(max_length=20,default='')
    
    def __str__(self):
        return self.name