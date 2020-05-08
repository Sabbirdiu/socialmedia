from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True,default='default.jpg')
    def __str__(self):
        return  f'{self.user.username} Profile'