from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user


class Advisor(models.Model):
    user = models.ForeignKey(Candidate, on_delete=models.CASCADE,related_name='user')
    booking_topic=models.CharField(max_length=64)
    advisor_name=models.CharField(max_length=20)
    def __str__(self):
        return self.advisor_name
