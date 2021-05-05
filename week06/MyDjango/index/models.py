from django.db import models

# Create your models here.

from django.db import models


class Type(models.Model):
    # id = models.AutoField(primary_key=True) # django会自动滚创建并设置为主键
    typename = models.CharField(max_length=20)


class Name(models.Model):
    # id 自动创建
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=10)
