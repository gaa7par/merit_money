from django.db import models

# Create your models here.


class Coworker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    avatar = models.ImageField(max_length=100)


class Kudo(models.Model):
    coworker = models.ForeignKey(Coworker, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    kudo = models.IntegerField(default=0)

