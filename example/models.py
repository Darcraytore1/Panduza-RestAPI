from django.db import models

MAX_LENGTH = 100

class Device(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)

    def __str__(self):
        return self.name
