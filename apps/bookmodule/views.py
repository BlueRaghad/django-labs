from django.shortcuts import render

def index(request):
    return render(request, "bookmodule/index.html")

def index2(request, val=0):
    return render(request, "bookmodule/index2.html", {"val": val})

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):        # ← pick bookId and stick with it
    book1 = {'id': 123, 'title': 'onePiece vol1', 'author': 'oda'}
    book2 = {'id': 124, 'title': 'onePiece vol2', 'author': 'oda'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

#lab5
def html5_links(request):
    return render(request, 'bookmodule/html5_links.html')

def html5_formatting(request):
    return render(request, 'bookmodule/html5_formatting.html')

def html5_listing(request):
    return render(request, 'bookmodule/html5_listing.html')

def html5_tables(request):
    return render(request, 'bookmodule/html5_tables.html')