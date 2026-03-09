from django.shortcuts import render

from django.shortcuts import render
# Create your views here.

def index(request):
    name = request.GET.get("name") or "World!"
    #return HttpResponse("hello, " + name)
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val = 0):
    return render(request, "bookmodule/index2.html",{"val": val})

def viewbook(request, bookID):
    book1 = {'id': 123, 'title': 'onePiece vol1', 'author': 'oda'}
    book2 = {'id': 124, 'title': 'onePiece vol2', 'author': 'oda'}

    targetBook = None
    if book1['id'] == bookID: targetBook = book1
    if book2['id'] == bookID: targetBook = book2
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)