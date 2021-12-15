from czytaj.models import Book, Author, ScreenAdaptation
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
def movie_example(example_book):
    return ScreenAdaptation.objects.create(
        book=example_book,
        movie="Example movie",
        director="Example director",
        year_of_premiere=1999,
        description="adsfasd adsf asd fads"
    )


@pytest.fixture
def example_movies(example_book):
    ScreenAdaptation.objects.create(book=example_book, movie="Example1", director="Sample1", year_of_premiere=2000,
                                    description="aaa aaaaa aaa")
    ScreenAdaptation.objects.create(book=example_book, movie="Example2", director="Sample2", year_of_premiere=2001,
                                    description="aaa aaaaa aaa")
    ScreenAdaptation.objects.create(book=example_book, movie="Example3", director="Sample3", year_of_premiere=2002,
                                    description="aaa aaaaa aaa")
