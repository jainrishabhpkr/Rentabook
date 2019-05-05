from django.shortcuts import render
from books.models import Book
from books.choices import category_choices, rating_choices

# Create your views here.

def indexview(request):
    book_list = Book.objects.order_by('-list_date').filter(is_published=True)[:3]
    mydict = {'books':book_list,'category_choices':category_choices,'rating_choices':rating_choices}
    return render(request,'pages/index.html',context=mydict)


def aboutview(request):
    return render(request,'pages/about.html')




def contactusview(request):
    return render(request,'pages/contactus.html')



def howitworksview(request):
    return render(request,'pages/howitworks.html')
