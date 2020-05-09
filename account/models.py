from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image
# Create your models here.

from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',default='default.jpg')
    def __str__(self):
        return  f'{self.user.username} Profile'