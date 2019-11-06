from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from book.models import Book

def index(request):
    if request.method == 'GET':
        return render(request,'book/index.html')
    else:
        username = request.POST.get('username')
        file_obj = request.FILES.get('file')
        print(file_obj)
        Book.objects.create(
            name = username,
            img = file_obj
        )
        return render(request,'book/index.html')

def disp(request):
    objs =Book.objects.all()
    return render(request,'book/disply.html',{'objs':objs})