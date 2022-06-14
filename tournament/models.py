from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start_time = models.DateField(blank=True, null=True)
    amountUsers = models.CharField(default=0, max_length=8)
    isFinished = models.BooleanField(default=False)
    loser = models.CharField(max_length=255, default='')
    winner = models.CharField(max_length=255, default='')
    winnerResult = models.CharField(max_length=255, default='')
    loserResult = models.CharField(max_length=255, default='')
