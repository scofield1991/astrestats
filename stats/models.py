from django.db import models

# Create your models here.
class Point(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Point_zn(models.Model):
    point=models.ForeignKey(Point)
    date=models.DateField()
    time=models.TimeField()
    zn=models.FloatField()

class Point_limit(models.Model):
    point=models.ForeignKey(Point)
    zn_morning=models.FloatField()
    zn_evening=models.FloatField()

class Zn_limit(models.Model):
    start_morning=models.TimeField()
    end_morning=models.TimeField()
    start_evening=models.TimeField()
    end_evening=models.TimeField()
