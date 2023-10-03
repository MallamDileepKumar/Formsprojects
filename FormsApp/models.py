from django.db import models

# Create your models here.
class Register(models.Model):
    FirstName = models.CharField(max_length=20)
    SecondName = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=15)
    ConfirmPassword = models.CharField(max_length=15)
    MobileNumber = models.IntegerField()

    def __str__(self):
        return self.FirstName