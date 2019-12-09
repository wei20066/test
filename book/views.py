from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from book.models import Book
from django.http import HttpResponse, HttpResponseRedirect
import csv



def index(request):
    return render(request,'book/index.html')



def upload(request):
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
    return HttpResponseRedirect('/book/disply/')
    #return render(request,'book/disply.html')

def disp(request):
    objs =Book.objects.all()
    return render(request,'book/disply.html',{'objs':objs})
   
   


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response