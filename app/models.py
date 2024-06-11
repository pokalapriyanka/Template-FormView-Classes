from django.db import models



class College(models.Model):
    Cname=models.CharField(max_length=100)
    Clocation=models.CharField(max_length=100)
    Cprincipal=models.CharField(max_length=100)
