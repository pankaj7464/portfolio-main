from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    def __str__(self):
        return self.email
        