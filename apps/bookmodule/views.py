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

#lab 6 
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]