
# Create your models here.

from django.db import models


class User(models.Model):
    username = models.CharField(
        verbose_name='username',
        max_length=20,
    )
    age = models.IntegerField(
        verbose_name='age',
    )
    sex = models.CharField(
        verbose_name='sex',
        max_length=6,
    )
class Bunka(models.Model):
    名称 = models.CharField(max_length=20,verbose_name="名称")
    緯度 = models.CharField(max_length=20,verbose_name="緯度")
    経度 = models.CharField(max_length=20,verbose_name="経度")
    文化財分類 = models.CharField(max_length=20,verbose_name="文化財分類")
    種類 = models.CharField(max_length=20,verbose_name="種類")
    数 = models.CharField(max_length=20,verbose_name="数")
    単位 = models.CharField(max_length=20,verbose_name="単位")
    愛媛県松山市住所 = models.CharField(max_length=20,verbose_name="愛媛県松山市住所")
    URL = models.CharField(max_length=20,verbose_name="URL")