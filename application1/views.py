from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def String_1(request):
    return HttpResponse("<h1>Hello Guysss....</h1>")
def Html_1(request):
     return render(request,'style1.html')
