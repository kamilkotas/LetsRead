from django.shortcuts import render, redirect
from django.views import View
from .models import Book, Author, Review, ScreenAdaptation, UserStory
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from czytaj.forms import LoginForm, AddUserForm, UserStoryForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin



class MainView(View):
    """
    Class displays the main view of the app.
    """
    def get(self, request):
        return render(request, "czytaj/index.html")


class ListOfBooksView(View):
    """
    Class shows the lists of books in database.
    """
    def get(self, request):
        books = Book.objects.all().order_by("tittle")
        counter = Book.objects.all().count()
        return render(request, 'czytaj/book_list.html', {"books": books, "counter": counter})


class BookView(View):
    """
    Class show details of the book.
    """
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        return render(request, "czytaj/book.html", {"book": book})


class AddBookView(LoginRequiredMixin, CreateView):
    """Form that adds a book to database"""
    login_url = "/login/"
    model = Book
    fields = ["tittle", "book_author", "year_of_publication", "publishing_house", "genre", "rating"]
    success_url = ("/books_list/")


class AuthorListView(View):
    """List of all the authors in database"""
    def get(self, request):
        authors = Author.objects.all().order_by("first_name")
        counter = Author.objects.all().count()
        return render(request, 'czytaj/author_list.html', {"authors": authors, "counter": counter})


class AddAuthorView(LoginRequiredMixin, CreateView):
    """Form that adds a book author to database"""
    login_url = "/login/"
    model = Author
    fields = "__all__"
    success_url = ("/authors_list/")


class AuthorView(View):
    """Shows a view of books author."""
    def get(self, request, author_id):
        author = Author.objects.get(id=author_id)
        return render(request, 'czytaj/author.html', {"author": author})


class AddReviewView(LoginRequiredMixin, CreateView):
    """Class creates form to add review to database."""
    login_url = "/login/"
    model = Review
    fields = "__all__"
    success_url = ("/books_list/")


class LoginView(View):
    """View that allows the user to login"""
    def get(self, request):
        form = LoginForm()
        return render(request, 'czytaj/login.html', {'form': form})

    def post(self, request):
        """Takes date from user authenticates it and logs in if user exists."""
        form = LoginForm(request.POST)
        form.is_valid()
        user = authenticate(username=form.cleaned_data['login'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'czytaj/login.html', {'form': form, 'message': 'Błędny login lub hasło'})


class LogoutView(View):
    """This view logs out the user."""
    def get(self, request):
        logout(request)
        return redirect('/')


class ReviewView(View):
    """Shows the review of books in the database if there are any."""
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        reviews = Review.objects.filter(book_id=book_id)
        return render(request, 'czytaj/review.html', {'book': book, "reviews": reviews})


class AddUserView(View):
    """Shows a view where you can register for the app."""
    def get(self, request):
        form = AddUserForm()
        return render(request, "czytaj/adduser.html", {"form": form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data["login"]
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            User.objects.create_user(
                                    username=login,
                                    password=password,
                                    first_name=first_name,
                                    last_name=last_name,
                                    email=email,
            )
            message = "Konto dodane do bazy danych"
            return render(request, "czytaj/adduser.html", {"form": form, "message": message})
        else:
            return render(request, "czytaj/adduser.html", {"form": form})


class ScreenAdaptationView(View):
    """Shows a view with movies based on the book."""
    def get(self, request):
        movies = ScreenAdaptation.objects.all()
        return render(request, "czytaj/movielist.html", {"movies": movies})


class MovieView(View):
    """Shows the view for a movie adaptation"""
    def get(self, request, movie_id):
        movie = ScreenAdaptation.objects.get(id=movie_id)
        return render(request, "czytaj/movies.html", {"movie": movie})


class AddMovieView(LoginRequiredMixin, CreateView):
    """Adds movie to database"""
    login_url = "/login/"
    model = ScreenAdaptation
    fields = "__all__"
    success_url = "/movielist/"


class UserStoryView(View):
    def get(self, request):
        user_text = UserStory.objects.all()
        return render(request, 'czytaj/users_storys.html', {"user_text": user_text})


class AddUserStoryView(LoginRequiredMixin, View):
    """The user can add things he wrote on our site"""
    login_url = "/login/"
    def get(self, request):
        form = UserStoryForm()
        return render(request, "czytaj/addstory.html", {"form": form})

    def post(self, request):
        form = UserStoryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['story']
            tittle = form.cleaned_data['tittle']
            story = UserStory.objects.create(author=request.user, story=content, tittle=tittle)
            story.save()
            return redirect("/user_story/")
        else:
            return render(request, "czytaj/addstory.html", {"form": form})
