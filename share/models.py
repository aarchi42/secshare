from django.db import models


class Verification(models.Model):
    email = models.EmailField(default='NA')
    verify = models.CharField(max_length=50)


class Images(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='share/images')

    def __str__(self):
        return self.name
