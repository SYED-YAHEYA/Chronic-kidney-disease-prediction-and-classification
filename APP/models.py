from django.db import models
from django.contrib.auth.models import User




class UserPredictModel(models.Model):
    image = models.ImageField(upload_to = 'images/')
    label = models.CharField(max_length=20,default='data')

    def __str__(self):
        return str(self.image)
    


   

from django.db import models

class Patient_info(models.Model):
    Bp = models.FloatField()
    Sg = models.FloatField()  # Example: consider using choices=(...) for gender
    Al = models.FloatField()
    Su = models.FloatField()
    Rbc = models.FloatField()
    Bu = models.FloatField()  # Example: consider using BooleanField for binary fields
    Sc = models.FloatField()
    Sod = models.FloatField()
    Pot = models.FloatField()
    Hemo = models.FloatField()
    Wbcc = models.FloatField()
    Rbcc = models.FloatField()
    Htn = models.FloatField()
    Class = models.CharField(max_length=100)

    def __str__(self):
        return f"Prediction: {self.Class}"

