from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserMobData(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mob_no = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.user

        
    


