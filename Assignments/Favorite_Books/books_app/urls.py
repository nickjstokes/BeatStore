from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('add', views.add),
    path('books/<int:id>', views.view_edit),
    path('books/<int:id>/edit', views.edit),
    path('books/<int:id>/view', views.view),
    path('favorite/<int:id>', views.favorite),
    path('unfavorite/<int:id>', views.unfavorite),
    path('favorite_other/<int:id>', views.favorite_other),
    path('books/<int:id>/update', views.update),
]