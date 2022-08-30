from django.db import models

# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name



class form(models.Model):
    first_name = models.CharField(max_length=250)
    last_name  = models.CharField(max_length=250)
    grnder=models.CharField(max_length=250)
    dateofbirth=models.CharField(max_length=250)
    phone_number=models.CharField(max_length=10)
    email=models.CharField(max_length=250)
    department=models.CharField(max_length=250)
    course=models.CharField(max_length=250)
    purpose=models.TextField()
    def __str__(self):
        return self.first_name


