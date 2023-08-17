from django.db import models

# Create your models here.

class Trainer(models.Model):
    t_name=models.CharField(max_length=50,primary_key=True)
    t_subject=models.CharField(max_length=30)
    t_age=models.IntegerField()