from django.db import models


class Flag(models.Model):
    country = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.country