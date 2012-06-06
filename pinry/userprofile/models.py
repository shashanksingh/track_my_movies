from django.db import models
from django.contrib.auth.models import User
     
class UserProfile(models.Model):
    url = models.URLField()
    firstname = models.CharField()
    lastname = models.CharField()
    home_address = models.TextField()
    phone_numer = models.PhoneNumberField()
    user = models.ForeignKey(User, unique=True)
