from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=32)
    date1 = models.DateTimeField(auto_now=True,null=True)
    date2 = models.DateTimeField(auto_now_add=True,null=True)
    img = models.ImageField(upload_to='img',null=True)