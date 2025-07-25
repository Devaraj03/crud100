from django.shortcuts import render,redirect,get_object_or_404  # type:ignore
from .models import book
from .forms import bookform

def index(request):
    books=book.objects.all()
    return render(request,'index.html',{'book':books})

def add(request):           
    form=bookform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'addbook.html',{'form':form})

def update(request,pk):
    books=get_object_or_404(book,pk=pk)
    form=bookform(request.POST or None,instance=books)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'update.html',{'form':form})

def delete(request,pk):
    books=get_object_or_404(book,pk=pk)
    if request.method=="POST":
        books.delete()
        return redirect('index')
    return render(request,'delete.html',{'book':books})