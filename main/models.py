from django.db import models

# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.title