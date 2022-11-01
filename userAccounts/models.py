from django.db import models
from django.contrib.auth.models import User
from .manager import UserManager
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=17,unique=True)
    email_verified = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)


# class Profile(models.Model):
#     user = models.OneToOneField(User ,on_delete=models.CASCADE)
#     mobile = models.CharField(max_length=20)
#     otp = models.CharField(max_length=6)



# class User(AbstractUser):
#     phone_number = models.CharField(max_length=12 , unique=True)
#     phone_verified = models.BooleanField(default=False)
#     otp = models.CharField(max_length=6)
#     USERNAME_FIELD = "phone_number"
#     REQUIRED_FIELDS = []
#     objects = UserManager()