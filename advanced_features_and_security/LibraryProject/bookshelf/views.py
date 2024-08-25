from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'book': books}

    def book_search(request):
        query = request.Get.get('q')
        if query:
            books = Book.objects.filter(title_icontains=query)
        else:
            books = Book.objects.all()
            return render(request, 'bookshelf/book_list.html', {'books': books})