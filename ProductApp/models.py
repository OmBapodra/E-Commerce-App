from django.db import models

# Create your models here.
class CatagoryModel(models.Model):
    name=models.CharField(max_length=100)
    catimage=models.ImageField(upload_to='catagory')

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    catagory=models.ManyToManyField(CatagoryModel)
    name=models.CharField(max_length=20)
    price=models.IntegerField(default=0)
    discription=models.TextField(max_length=200)
    image=models.ImageField(upload_to='product')

    def __str__(self):
        return self.name