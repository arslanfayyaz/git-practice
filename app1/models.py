from django.db import models
from datetime import datetime, timedelta


class Event(models.Model):
    name = models.CharField(max_length=50)
    event_date = models.DateTimeField()

