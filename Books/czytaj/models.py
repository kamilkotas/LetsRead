from django.db import models

# Create your models here.

STARS = (
    (1, "*"),
    (2, "**"),
    (3, "***"),
    (4, "****"),
    (5, "*****"),
)


GENRE = (
    (1, "klasyka"),
    (2, "horror"),
    (3, "kryminał"),
    (4, "romans"),
    (5, "literatura piękna"),
    (6, "biografia"),
    (7, "reportaż"),
    (8, "poezja"),
)


class Author(models.Model):
    first_name = models.CharField(max_length=128, verbose_name="Imię")
    last_name = models.CharField(max_length=128, verbose_name="Nazwisko")
    year_of_birth = models.DateField(verbose_name="Rok urodzenia")
    year_of_death = models.DateField(verbose_name="Rok śmierci", help_text="opcjonalnie: jeżeli nie żyje", default=None, null=True, blank=True)
    books = models.ManyToManyField("Book")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    tittle = models.CharField(max_length=256, verbose_name="Tytuł")
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE, max_length=256, verbose_name="Autor")
    year_of_publication = models.IntegerField(verbose_name="Rok publikacji")
    publishing_house = models.CharField(max_length=256, verbose_name="Wydawnictwo")
    genre = models.IntegerField(choices=GENRE, verbose_name="Gatunek")
    rating = models.IntegerField(choices=STARS, verbose_name="Ocena")

    def __str__(self):
        return self.tittle


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Książka")
    review = models.TextField(verbose_name="Recenzja")

