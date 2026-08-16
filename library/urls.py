from django.urls import path

from . import views


urlpatterns = [
    path("", views.hello, name="hello"),
    path("books/", views.book_list, name="book_list"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
]