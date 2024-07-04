from django.db import models

# Create your models here.
class EmpModel(models.Model):
    eid= models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=25)
    ecity = models.CharField(max_length=25)
    esal = models.FloatField()
    eemail = models.EmailField()
    edept= models.CharField(max_length=20)

