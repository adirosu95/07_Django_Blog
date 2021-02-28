from django.db import models
from django.utils import timezone


# Create your models here.

class NewsletterUser(models.Model):
    email = models.EmailField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Newsletter subscriber email: {self.email}"