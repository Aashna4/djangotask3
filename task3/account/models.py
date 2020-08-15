from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    phno = models.IntegerField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

