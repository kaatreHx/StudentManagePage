from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.IntegerField()
    semester = models.CharField(max_length=50)
    profilePic = models.ImageField(upload_to='profile_pics/', max_length=255, default='profile_pics/default.jpg') 

    def __str__(self):
        return f"{self.name} + {self.address} + {self.contact} + {self.semester}"
