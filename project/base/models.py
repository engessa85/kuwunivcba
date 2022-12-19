from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    serialNumber = models.CharField(max_length=100, null=True)
    teaching = models.BooleanField(default=False, null=True)
    vip = models.BooleanField(default=False, null=True)
    report = models.CharField(max_length=10, null=True)
    REQUIRED_FIELDS = []


class DT_model(models.Model):
    days_choices =[("24", "24"),
                   ("135", "135"),
                   ("12345", "12345")]

    group = models.CharField(max_length=100, null= True, choices=days_choices)
    time_value = models.CharField(max_length=100, null= True, unique=True)
    def __str__(self):
        return str(self.time_value)


class Courses_model(models.Model):
    title = models.CharField(max_length=100, null=True, unique=True)
    number = models.CharField(max_length=100, null=True, unique=True)
    offered = models.BooleanField(default=True, null=True)
    credit = models.PositiveIntegerField(null=True)
    # 
    def __str__(self):
        return str(self.title)

class Days_model(models.Model):
    title = models.CharField(max_length=100, null=True, unique=True)
    def __str__(self):
        return str(self.title)



class Desires_model(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    d1 = models.CharField(max_length=100, null=True)
    d1t1 = models.CharField(max_length=100, null=True)
    d1t2 = models.CharField(max_length=100, null=True)
    d1t3 = models.CharField(max_length=100, null=True)
    day1 = models.CharField(max_length=100, null=True)

    d2 = models.CharField(max_length=100, null=True)
    d2t1 = models.CharField(max_length=100, null=True)
    d2t2 = models.CharField(max_length=100, null=True)
    d2t3 = models.CharField(max_length=100, null=True)
    day2 = models.CharField(max_length=100, null=True)

    d3 = models.CharField(max_length=100, null=True)
    d3t1 = models.CharField(max_length=100, null=True)
    d3t2 = models.CharField(max_length=100, null=True)
    d3t3 = models.CharField(max_length=100, null=True)
    day3 = models.CharField(max_length=100, null=True)

    d4 = models.CharField(max_length=100, null=True)
    d4t1 = models.CharField(max_length=100, null=True)
    d4t2 = models.CharField(max_length=100, null=True)
    d4t3 = models.CharField(max_length=100, null=True)
    day4 = models.CharField(max_length=100, null=True)

    d5 = models.CharField(max_length=100, null=True)
    d5t1 = models.CharField(max_length=100, null=True)
    d5t2 = models.CharField(max_length=100, null=True)
    d5t3 = models.CharField(max_length=100, null=True)
    day5 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.user)


class Semester_files(models.Model):
    file = models.FileField(blank = False, null=True)

    def __str__(self):
        return str(self.file.name)
        
    def delete(self,*args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    


    


    