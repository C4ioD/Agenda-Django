from django.db import models
from django.utils import timezone

# Create your models here.

class Catagory(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name
  



class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Catagory, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
      return self.first_name + ' ' + self.last_name
  