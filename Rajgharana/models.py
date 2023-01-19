from django.db import models


class Register(models.Model): 
    regid=models.AutoField (primary_key=True)
    email=models.CharField(max_length=50) 
    password=models.CharField(max_length=15)  
    status=models.IntegerField()
    role=models.CharField(max_length=10) 
    info=models.CharField(max_length=50)

class Invaild_Register_users(models.Model): 
    regid=models.AutoField (primary_key=True)
    email=models.CharField(max_length=50) 
    password=models.CharField(max_length=15)  
    status=models.IntegerField()
    role=models.CharField(max_length=10) 
    info=models.CharField(max_length=50)   

class Login(models.Model): 
    regid=models.AutoField (primary_key=True)
    email=models.CharField(max_length=50) 
    password=models.CharField(max_length=15)  
    status=models.IntegerField()
    role=models.CharField(max_length=10)
    info=models.CharField(max_length=50)   

class Invaild_Login_users(models.Model): 
    regid=models.AutoField (primary_key=True)
    email=models.CharField(max_length=50) 
    password=models.CharField(max_length=15)  
    status=models.IntegerField()
    role=models.CharField(max_length=10) 
    info=models.CharField(max_length=50)
   