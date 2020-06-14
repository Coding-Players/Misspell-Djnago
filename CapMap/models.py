from django.db import models


class MapLocation(models.Model):
    latitude = models.FloatField(max_length=18)
    longitude = models.FloatField(max_length=18)
    pop_up_text = models.CharField(max_length=45)

    def __str__(self):
        return self.pop_up_text
