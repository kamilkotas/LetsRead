from czytaj.models import Book, Author
from django.contrib.auth.models import User
import pytest

@pytest.fixture
def example_author():
    return Author.objects.create(
        first_name="Fiodor",
        last_name="Dostojewski",
        year_of_birth="1900-10-10",
        year_of_death="1980-01-01",
    )


@pytest.fixture
def example_book(example_author):
     return Book.objects.create(
                                tittle="Example_book",
                                book_author=example_author,
                                year_of_publication=2000,
                                publishing_house="Świat Książki",
                                genre=1,
                                rating=5,
    )


@pytest.fixture
def parent_user():
    user = User.objects.create_user('parent', 'parentpassword')
    return user


@pytest.fixture
def examples_of_books(example_author):
    Book.objects.create(tittle="Example1", book_author=example_author, year_of_publication=1990, publishing_house="Świat Książki", genre=3, rating=4)
    Book.objects.create(tittle="Example2", book_author=example_author, year_of_publication=1990, publishing_house="Świat Książki", genre=3, rating=4)
    Book.objects.create(tittle="Example3", book_author=example_author, year_of_publication=1990, publishing_house="Świat Książki", genre=3, rating=4)
    Book.objects.create(tittle="Example4", book_author=example_author, year_of_publication=1990, publishing_house="Świat Książki", genre=3, rating=4)
    Book.objects.create(tittle="Example5", book_author=example_author, year_of_publication=1990, publishing_house="Świat Książki", genre=3, rating=4)
