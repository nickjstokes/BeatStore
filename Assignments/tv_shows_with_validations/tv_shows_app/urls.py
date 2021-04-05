from django.urls import path
from . import views
urlpatterns = [
    path('', views.redirect_home),
    path('shows', views.index),
    path('shows/<int:id>', views.read_one),
    path('shows/<int:id>/edit', views.edit),
    path('shows/new', views.add),
    path('create', views.create),
    path('update/<int:id>', views.update),
    path('shows/<int:id>/destroy', views.delete)
]