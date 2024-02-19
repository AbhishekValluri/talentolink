from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class contact(models.Model): # table name in mysql database models.model is a library to create a table in mysql database
    # column defination
    # columnName=datatype(required fields)
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=50,null=False)
    mobile=models.BigIntegerField(null=False)
    description=models.CharField(max_length=100,null=True)



    class Meta:
         db_table='contacts'  # in database it will store as contact.models.model to change the name we write this line of code.


class profile(models.Model):

    User=models.OneToOneField(User,on_delete=models.CASCADE)
    mobile=models.BigIntegerField(null=False) 

    def __str__(self):
        return self.User.username

# post a job
    
class PostJobs(models.Model):

    jobtitle=models.CharField(max_length=100,null=False)
    Companyname=models.CharField(max_length=150,null=False)
    Numofvacancies=models.BigIntegerField(null=False)
    location=models.CharField(max_length=100,null=True)
    Jobdescription=models.CharField(max_length=150,null=True)
    Salary=models.CharField(max_length=100,null=True)
    # image=models.ImageField(upload_to='uploads/images/')

class Meta:
    db_table='postjobs'




# Employeers login
    
class employee(models.Model):
    Userid=models.CharField(max_length=100,null=False)
    Companyname=models.CharField(max_length=150,null=False)
    password=models.CharField(max_length=100,null=False)


class Meta:
    db_table='employees'






