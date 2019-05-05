from django.db import models
from datetime import datetime
from authors.models import Author

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING,related_name=None)
    title = models.CharField(max_length=400)
    format = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    bookcode = models.CharField(max_length=400, blank=True)
    no_of_pages = models.IntegerField()
    publication = models.CharField(max_length=400, blank=True)
    description = models.TextField(blank=True)
    Ratings = models.DecimalField(max_digits=2,decimal_places=1)
    price = models.IntegerField()
    is_donated = models.BooleanField()
    donated_by = models.CharField(max_length=100, blank=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
