from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return "%s %s" %(self.first_name,self.last_name)
