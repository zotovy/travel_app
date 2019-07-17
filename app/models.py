from django.conf import settings
from django.db import models
from django.utils import timezone


class Notification(models.Model):

    # Notification param
    number = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    departure_place = models.CharField(max_length=100)
    arrival_place = models.CharField(max_length=100)
    min_day = models.IntegerField()
    max_day = models.IntegerField()
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    vacation_start = models.DateField()
    vacation_end = models.DateField()
    notification_frequency = models.CharField(max_length=100)
    go_speed = models.IntegerField()    # переодичность, 1-5




