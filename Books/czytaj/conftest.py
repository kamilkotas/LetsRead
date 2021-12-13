from .models import Book, Author

import pytest

# @pytest.fixture
# def example_book():
#     return Book.objects.create(
#                                 tittle="Example_book",
#                                 book_author=Author.objects.create(
#                                                                 first_name='Example',
#                                                                 last_name='Sample',
#                                 ),
#                                 year_of_publication=2000,
#                                 publishing_house="Świat Książki",
#                                 genre=1,
#                                 rating=5,
#     )