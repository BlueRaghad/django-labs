from django.shortcuts import render

from django.shortcuts import render
# Create your views here.

def index(request):
    name = request.GET.get("name") or "World!"
    #return HttpResponse("hello, " + name)
    return render(request, "bookmodule/index.html")

#def index2(request, val = 0):
 #   return HttpResponse("value = " + str(val))