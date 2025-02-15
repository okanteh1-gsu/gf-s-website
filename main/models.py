from django.db import models

class HerInfo(models.Model):
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

class RomanticImage(models.Model):
    about_image = models.ImageField(null=True, blank=True)