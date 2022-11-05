from django.db import models



# Create your models here.

class Doctor (models.Model):
    id = models.IntegerField(primary_key=True )
    name = models.TextField(max_length=200 , blank=False , null=False)
    Med_rec_no = models.IntegerField(blank=False , null=False)
    spec = models.TextField(max_length=200 , null=True , blank=True)
    hosp_name = models.TextField(max_length=200 , blank=False , null=False)
    exp = models.TextField(max_length=200 ,  blank=False , null=False)