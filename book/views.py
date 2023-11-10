from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def get_all_book(request):
    books = Book.objects.all()
    return render(request, 'homepage.html', {'books': books})


def add_new_book(request):
    form = BookForm()
    if request.method == "POST":
        book = BookForm(request.POST)
        if book.is_valid():
            book.save()
            return redirect("/")
    return render(request, 'book.html', {"form": form})


def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)
    if request.method == "POST":
        updated_book = BookForm(request.POST, instance=book)
        if updated_book.is_valid():
            updated_book.save()
            return redirect("/")
    return render(request, 'update_book.html', {"form": form})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    if book:
        book.delete()
        return redirect("/")
