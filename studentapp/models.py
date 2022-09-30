from django.db import models

# Create your models here.
class addstudent(models.Model):
    student_name=models.CharField(max_length=255)
    email=models.EmailField()
    phone_number=models.IntegerField()
    address=models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/", null=True)