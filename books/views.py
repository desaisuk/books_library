from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib import messages


def home(request):
    return render(request, 'books/home.html')


def searchBook(request):
    if request.method == "GET" and 'book_name' in request.GET:
        search_query = request.GET.get('search_box1',None)
        books = Book.objects.filter(name__iexact=search_query)
        print(books)
        no_record_flag = False
        if search_query and books.count() == 0:
            no_record_flag = True

        if books.count() != 0:
            context = {
                'books' : books
            }
            return render(request, 'books/searchBook.html', context)
        else:
            context = {
                'no_record_flag' : no_record_flag
            }
            return render(request, 'books/searchBook.html', context)
    
    if request.method == "GET" and 'book_publishdate' in request.GET:
        search_query = request.GET.get('search_box2',None)
        books = Book.objects.filter(publish_year__iexact=search_query)
        no_record_flag = False
        if search_query and books.count() == 0:
            no_record_flag = True

        if books.count() != 0:
            context = {
                'books' : books
            }
            return render(request, 'books/searchBook.html', context)
        else:
            context = {
                'no_record_flag' : no_record_flag
            }
            return render(request, 'books/searchBook.html', context)
    
    return render(request, 'books/searchBook.html', {})


def updateInfo(request):
    if request.method == "GET":
        qs = Book.objects.all()
        search_query = request.GET.get('search_box',None)
        books = qs.filter(name__iexact=search_query).first()
        form = BookForm(instance=books)
        
        no_record_flag = False
        if search_query and books:
            no_record_flag = True

        if books:
            context = {
                'books' : books,
                'form' : form
            }
            return render(request, 'books/updateInfo.html', context)
        else:
            context = {
                'no_record_flag' : no_record_flag
            }
            return render(request, 'books/updateInfo.html', context)
    

    if request.method == "POST":
        
        name = request.body.decode('utf-8').split('&')[2].split('=')[1].replace('+',' ').replace('%2C',',')
        qs = Book.objects.all()
        Book.objects.filter(name__iexact=name).delete()
        
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Book information updated!')
            return redirect('books-home')
        else:
            books = qs.filter(name__iexact=name).first()
            context = {
                'books' : books,
                'form' : form
            } 
            return render(request, 'books/updateInfo.html', context) 

        return render(request, 'books/updateInfo.html', {'form':form}) 

    return render(request, 'books/updateInfo.html', {})



def addBook(request):
    form = BookForm()

    if request.method == "POST":
                
        form = BookForm(request.POST)
        if form.is_valid():
            print("Valid")
            form.save()
            messages.success(request, f'New book added!')
            return redirect('books-home')
    
    return render(request, 'books/addBook.html',  {'form':form})