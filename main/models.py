from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=500)
    website=models.URLField()

# Create your models here.
class Banner(models.Model):
    img=models.ImageField()
    title=models.CharField(max_length=300)
    body=models.TextField()
    description=models.CharField(max_length=3000)



class Our_Services(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    services=models.CharField(max_length=300)


class Technicians(models.Model):
    img=models.ImageField()
    title=models.CharField(max_length=300)
    instagram=models.URLField()
    facebook=models.URLField()
    twitter=models.URLField()


class Address(models.Model):
    address=models.CharField(max_length=500)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    website=models.URLField()
    def __str_(self):
        return self.address


class Opening_Hours(models.Model):
    day=models.CharField(max_length=100)
    start_time=models.TimeField()
    end_time=models.TimeField()


class Newsletter(models.Model):
    title=models.CharField(max_length=400)
    email=models.EmailField()

    