from django.db import models


class Clock(models.Model):
    time_sent = models.DateTimeField()
    time_received= models.DateTimeField()
    time_processed = models.DateTimeField()