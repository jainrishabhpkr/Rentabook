from django.shortcuts import render, get_object_or_404
from books.models import Book
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

# Create your views here.
def indexview(request):
    book_list=Book.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(book_list,6)
    page_no = request.GET.get('page')
    try:
        book_list = paginator.page(page_no)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)
    mydict={'books':book_list}

    return render(request,'books/books.html',context=mydict)

def bookview(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    my_dict = {'book':book}
    return render(request,'books/book.html',context=my_dict)


def searchview(request):
    queryset_list = Book.objects.all()

    #keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(title__icontains=keywords)

    #authors
    if 'author' in request.GET:
        author=request.GET['author']
        if author:
            queryset_list = queryset_list.filter(author__icontains=author)

    #ratings
    if 'ratings' in request.GET:
        ratings=request.GET['ratings']
        if author:
            queryset_list = queryset_list.filter(Ratings__gte=ratings)

    #price
    if 'price' in request.GET:
        price=request.GET['price']
        if author:
            queryset_list = queryset_list.filter(price__lte=price)


    my_dict={'books':queryset_list}
    return render(request,'books/search.html',context=my_dict)
