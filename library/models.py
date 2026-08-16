from django.db import models


# 학과
class Department(models.Model):
    depart_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# 회원
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)

    google_sub = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


# 도서 메타 정보
class Book(models.Model):
    book_id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=300)

    author = models.CharField(max_length=200)

    translator = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    category = models.CharField(
        max_length=100,
        blank = True,
    )

    publisher = models.CharField(
        max_length=200,
        blank=True,
    )

    publish_date = models.DateField(
        null=True,
        blank=True
    )


    def __str__(self):
        return self.name


# 실제 소장 도서 한 권
class BookCopy(models.Model):

    class Condition(models.TextChoices):
        NORMAL = "NORMAL", "정상"
        DAMAGED = "DAMAGED", "파손"
        LOST = "LOST", "분실"
        DISCARDED = "DISCARDED", "폐기"

    label_code = models.CharField(
        max_length=100,
        primary_key=True
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name="copies"
    )

    condition = models.CharField(
        max_length=20,
        choices=Condition.choices,
        default=Condition.NORMAL
    )

    location = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f"{self.book.name} ({self.label_code})"


# 대여 기록
class Rental(models.Model):
    rental_id = models.BigAutoField(primary_key=True)

    book_copy = models.ForeignKey(
        BookCopy,
        on_delete=models.PROTECT,
        related_name="rentals"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="rentals"
    )

    rental_date = models.DateTimeField(
        auto_now_add=True
    )

    return_date = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.name} - {self.book_copy.label_code}"