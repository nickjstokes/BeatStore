from django.urls import path
from . import views
from .models import Books, Authors

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('book/<int:id>', views.view_book),
    path('authors', views.authors),
    path('add_author_to_book<int:id>', views.add_author),
    path('authors/<int:id>', views.view_author)
]