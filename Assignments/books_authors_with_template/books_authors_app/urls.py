from django.urls import path
from . import views
from .models import Books, Authors

urlpatterns = [
    path('', views.index),
    path('books', views.index),
    path('add_book', views.add_book),
    path('book/<int:id>', views.view_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('add_author_to_book/<int:book_id>', views.add_author_to_book),
    path('add_book_to_author/<int:author_id>', views.add_book_to_author),
    path('authors/<int:id>', views.view_author)
]