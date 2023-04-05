from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item_detail", args=[str(self.id)])
    
