from django.contrib import admin
from authors.models import Author
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')
    list_display_links=('first_name','last_name')

admin.site.register(Author,AuthorAdmin)
