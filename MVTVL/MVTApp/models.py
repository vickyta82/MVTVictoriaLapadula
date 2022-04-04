from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField(primary_key=True)
    birthday = models.DateField(max_length=10)
    email = models.EmailField()





