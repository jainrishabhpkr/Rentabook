from django.contrib import admin
from books.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','author','price','Ratings','category','format')
    list_display_links =('id','title')
    list_filter = ('author',)
    list_editable=('is_published',)
    search_fields=('title','author','format','category')
    list_per_page=25

admin.site.register(Book,BookAdmin)
