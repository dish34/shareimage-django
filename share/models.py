from django.db import models

# Create your models here.
class Image(models.Model):
    title       = models.CharField(max_length=20)
    description = models.TextField()
    img         = models.ImageField(upload_to="imag") 