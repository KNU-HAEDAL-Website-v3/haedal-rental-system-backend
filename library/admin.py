from django.contrib import admin

from .models import (
    Department,
    User,
    Book,
    BookCopy,
    Rental,
)


admin.site.register(Department)
admin.site.register(User)
admin.site.register(Book)
admin.site.register(BookCopy)
admin.site.register(Rental)