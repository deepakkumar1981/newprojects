from django.db import models

# Crate your models here.


class Pages(models.Model):

    text = models.TextField()

    def __str__(self):
        return self.text[:5000]
