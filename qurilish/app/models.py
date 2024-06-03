from django.db import models


class Hudud(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
    
class QurilishTashkiloti(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    opened_at = models.DateField()
    hudud = models.ForeignKey(Hudud, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return self.name
    

class Qurilish(models.Model):
    qurilish_tashkiloti = models.ForeignKey(QurilishTashkiloti, on_delete=models.DO_NOTHING)
    hudud = models.ForeignKey(Hudud, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    maydoni = models.DecimalField(max_digits=20, decimal_places=2)
    qavat = models.IntegerField(default=1)
    parking = models.BooleanField(default=True)
    child_place = models.BooleanField(default=True)
    elevator = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    

