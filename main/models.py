from django.db import models

# Create your models here.


class professor(models.Model):
    name=models.CharField(max_length=20)
    # numbers=models.IntegerField()


    def __str__(self):
        return self.name
    


class student(models.Model):
    name=models.CharField(max_length=20)
    professors=models.ForeignKey(professor,on_delete=models.CASCADE)


    def __str__(self):
        return self.name