from django.db import models


class OutdoorPlan(models.Model):
    # Images
    image = models.ImageField(upload_to='images/')
    # Summary
