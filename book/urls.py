from django.urls import path
from .views import add_new_book, update_book, delete_book, get_all_book

urlpatterns = [
    path("", get_all_book, name='book_list'),
    path("update/book/<int:id>", update_book, name="update_book"),
    path("delete/book/<int:id>", delete_book, name="delete_book"),
    path("add/book", add_new_book, name="add_book"),
]
