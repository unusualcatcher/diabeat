from django.db import models

class HealthLog(models.Model):
    pregnancies = models.FloatField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    age = models.IntegerField()
    diabetes_prediction = models.FloatField()
    date_created = models.DateField()

    def __str__(self):
        return f"Health Log: {self.age} years old"

