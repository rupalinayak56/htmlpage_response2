from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def String_3(request):
    return HttpResponse("<h1><marquee>🙂Being Happy is greatest form of success..🙂</marquee></h1>")
def Html_3(request):
    return render(request,'style3.html')
