from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('add_job', views.add_job),
    path('add', views.add),
    path('cancel', views.cancel),
    path('remove/<int:id>', views.remove),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('view/<int:id>', views.view),
    # path('books/<int:id>', views.view_edit),
    # path('books/<int:id>/edit', views.edit),
    # path('books/<int:id>/view', views.view),
    # path('favorite/<int:id>', views.favorite),
    # path('unfavorite/<int:id>', views.unfavorite),
    # path('favorite_other/<int:id>', views.favorite_other),
    # path('books/<int:id>/update', views.update),
]