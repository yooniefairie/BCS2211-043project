from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Mentor(models.Model):
    menid=models.CharField(max_length=8, primary_key=True)
    menname=models.TextField(max_length=225)
    menroomno=models.CharField(max_length=3, default='sk2')