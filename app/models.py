from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('contact')
