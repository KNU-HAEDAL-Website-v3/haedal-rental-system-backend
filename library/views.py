from django.shortcuts import get_object_or_404, render

from .models import Book


def hello(request):

    return render(
        request,
        "library/hello.html",
        {}
    )


def book_list(request):
    books = Book.objects.all()

    return render(
        request,
        "library/tembook_list.html",
        {"books": books}
    )


def book_detail(request, book_id):
    book = get_object_or_404(
        Book,
        book_id=book_id
    )

    return render(
        request,
        "library/book_detail.html",
        {"book": book}
    )