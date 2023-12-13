from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser, models.Model):
    phone_number = models.CharField(max_length=13)
    Lavozimi = models.ForeignKey('Lavozimlar', on_delete = models.CASCADE, null =True, blank = True)

class Lavozimlar(models.Model):
    name = models.CharField(max_length=50, help_text="Faqatgina lavozimning nomini kiriting")

    def __str__(self):
        return self.name
    