from django.db import models

# Create your models here.
class Point(models.Model):
    name=models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Point_zn(models.Model):
    point=models.ForeignKey(Point)
    dtime=models.DateTimeField()
    zn=models.FloatField()

