from django.db import models


class MapLocation(models.Model):
    latitude = models.FloatField(max_length=18)
    longitude = models.FloatField(max_length=18)

    def __float__(self):
        return "Latitude:" + self.latitude + " Longitude:" + self.longitude
