from django.db import models

# Create your models here.
class StudentData(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.IntegerField()
    semester = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}+ {self.address} + {self.contact} + {self.semester}"
    