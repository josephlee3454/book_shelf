from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.




def make_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    objs = Book.objects.all()
    context = {'form':form, 'objs':objs}
    return render(request, 'index.html',context)



def make_author(request):
    second_form = AuthorForm()
    if request.method == 'POST':
        second_form = AuthorForm(request.POST)
        if second_form.is_valid():
            second_form.save()
    objs = Author.objects.all()
    context = {'second_form':second_form, 'objs':objs}
    return render(request, 'authors.html',context)

def view_book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'author_book': Book.objects.get(id=book_id).authors.all(),
        'all_authors': Author.objects.all()
    }
    
    return render(request, 'view_book.html', context)

def view_author(request, author_id):
    context = {
        'author': Author.objects.get(id=author_id),
        'book_author': Author.objects.get(id=author_id).books.all(),
        'all_books': Book.objects.all()
    }
    return render(request, 'view_author.html', context)