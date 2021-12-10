"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from czytaj.views import (MainView, ListOfBooksView, BookView, AddBookView, AuthorListView, AddAuthorView, AuthorView,
                          LoginView, LogoutView, AddReviewView, ReviewView, AddUserView, ScreenAdaptationView, MovieView, AddMovieView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('books_list/', ListOfBooksView.as_view(), name="book-list"),
    path('book/<int:book_id>/', BookView.as_view(), name="book"),
    path('add_book/', AddBookView.as_view(), name="add-book"),
    path('authors_list/', AuthorListView.as_view(), name="author-list"),
    path('add_author/', AddAuthorView.as_view(), name='add-author'),
    path('author/<int:author_id>/', AuthorView.as_view(), name='author'),
    path('add_review/', AddReviewView.as_view(), name="review"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view()),
    path('review/<int:book_id>/', ReviewView.as_view()),
    path('add_user/', AddUserView.as_view(), name="add-usser"),
    path('movielist/', ScreenAdaptationView.as_view()),
    path('movie/<int:movie_id>/', MovieView.as_view()),
    path('add_movie/', AddMovieView.as_view()),
]
