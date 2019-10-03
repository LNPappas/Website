from django.db import models

# Create your models here.
class SignForm(models.Model):
    first = models.CharField(max_length=264)
    last = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)
    company = models.CharField(max_length=264)

    def __str__(self):
        return self.first + " " + self.last
    