import datetime

from django.test import Client
from .models import Book, Author, Review
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth.models import User
import pytest


def test_main_site_status(client):
    response = client.get("/")
    assert response.status_code == 200
    assertTemplateUsed(response, "czytaj/index.html")


@pytest.mark.django_db
def test_books_list_view(client, examples_of_books):
    response = client.get("/books_list/", examples_of_books)
    assert response.status_code == 200
    assertTemplateUsed(response, 'czytaj/book_list.html')
    assert len(response.context['books']) == Book.objects.all().count()


@pytest.mark.django_db
def test_book(client, example_book, example_author):
    response = client.get(f"/book/{example_book.id}/")
    assert response.status_code == 200
    assert response.context['book'].tittle == "Example_book"
    assert response.context['book'].book_author == example_author
    assert response.context['book'].year_of_publication == 2000
    assert response.context['book'].publishing_house == "Świat Książki"
    assert response.context['book'].genre == 1
    assert response.context['book'].rating == 5


@pytest.mark.django_db
def test_add_book(client, example_author, parent_user):
    client.force_login(parent_user)
    response = client.post(f'/add_book/',
                           {"tittle": 'Example', "book_author": {example_author.id}, "year_of_publication": 1880,
                            "publishing_house": "Świat książki", "genre": 5, "rating": 3})
    assert response.status_code == 302
    book = Book.objects.get(tittle='Example')
    assert book.book_author == example_author
    assert book.year_of_publication == 1880
    assert book.publishing_house == "Świat książki"
    assert book.genre == 5
    assert book.rating == 3


@pytest.mark.django_db
def test_authors_list_site_template(client):
    response = client.get("/authors_list/")
    assert response.status_code == 200
    assertTemplateUsed(response, 'czytaj/author_list.html')


@pytest.mark.django_db
def test_add_author(client, parent_user):
    client.force_login(parent_user)
    response = client.post('/add_author/',
                           {"first_name": 'Example', "last_name": 'Sample', "year_of_birth": "1990-12-10"})
    assert response.status_code == 302
    author = Author.objects.get(last_name='Sample')
    assert author.first_name == 'Example'
    assert author.year_of_birth == datetime.date(1990, 12, 10)


@pytest.mark.django_db
def test_author(client, example_author):
    response = client.get(f"/author/{example_author.id}/")
    assert response.status_code == 200
    assert response.context["author"].first_name == "Fiodor"
    assert response.context['author'].last_name == "Dostojewski"
    assert response.context['author'].year_of_birth == datetime.date(1900, 10, 10)
    assert response.context['author'].year_of_death == datetime.date(1980, 1, 1)


@pytest.mark.django_db
def test_review(client, example_book, parent_user):
    client.force_login(parent_user)
    response = client.post("/add_review/", {"book": example_book.id, "tittle": "Kto to czyta", "review": "Ta książka jest słaba"})
    assert response.status_code == 302
    user_review = Review.objects.get(book=example_book)
    assert user_review.tittle == "Kto to czyta"
    assert user_review.review == "Ta książka jest słaba"


@pytest.mark.django_db
def test_add_user(client):
    response = client.post("/add_user/", {"login": "Example", "password": "myszykiszki1", "password2": "myszykiszki1",
                                          "first_name": "Anon", "last_name": "Anonimowy", "email": "Anon@gmail.com"})
    assert response.status_code == 200
    new_user = User.objects.get(username="Example")
    assert new_user.first_name == "Anon"
    assert new_user.last_name == "Anonimowy"
    assert new_user.email == "Anon@gmail.com"





