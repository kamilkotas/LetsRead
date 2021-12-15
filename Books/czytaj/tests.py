import datetime

from django.test import Client
from .models import Book, Author, Review, ScreenAdaptation, UserStory
from pytest_django.asserts import assertTemplateUsed
from django.contrib.auth.models import User
import pytest


def test_main_site_status(client):
    response = client.get("/")
    assert response.status_code == 200
    assertTemplateUsed(response, "czytaj/index.html")


@pytest.mark.django_db
def test_books_list_view(client, ):
    response = client.get("/books_list/")
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


@pytest.mark.django_db
def test_login_user(client):
    client.post("/add_user/", {"login": "Example", "password": "myszykiszki1", "password2": "myszykiszki1",
                                "first_name": "Anon", "last_name": "Anonimowy", "email": "Anon@gmail.com"})
    response = client.post('/login/', {"login": 'Example', "password": 'myszykiszki1'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_screen_adaptation(client, example_movies):
    response = client.get('/movielist/', example_movies)
    assert response.status_code == 200
    assert len(response.context['movies']) == ScreenAdaptation.objects.all().count()
    assertTemplateUsed('czytaj/movielist.html')


@pytest.mark.django_db
def test_movie_view(client, movie_example, example_book):
    response = client.get(f"/movie/{movie_example.id}", {}, True)
    print(response.content)
    assert response.status_code == 200
    assert response.context['movie'].book == example_book
    assert response.context['movie'].movie == "Example movie"
    assert response.context['movie'].director == "Example director"
    assert response.context['movie'].year_of_premiere == 1999
    assert response.context['movie'].description == "adsfasd adsf asd fads"


@pytest.mark.django_db
def test_add_movie(client, example_book, parent_user):
    client.force_login(parent_user)
    response = client.post("/add_movie/", {"book": example_book.id, "movie": "Example movie", "director": "Woody Allen",
                                "year_of_premiere": 2021, "description": "Ale gniot"})
    print(response.content)
    assert response.status_code == 302
    movie = ScreenAdaptation.objects.get(movie="Example movie")
    assert movie.book == example_book
    assert movie.director == "Woody Allen"
    assert movie.year_of_premiere == 2021
    assert movie.description == "Ale gniot"


@pytest.mark.django_db
def test_user_story(client):
    response = client.get("/user_story/")
    assert response.status_code == 200
    assertTemplateUsed("czytaj/user_storys.html")


@pytest.mark.django_db
def test_add_story(client, parent_user):
    client.force_login(parent_user)
    response = client.post("/add_story/", {"tittle": "Historia", "story": "O to moja historia..."})
    assert response.status_code == 302
    text = UserStory.objects.get(tittle="Historia")
    assert text.story == "O to moja historia..."
    assert text.author == parent_user






