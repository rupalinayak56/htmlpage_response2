from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def String_2(request):
    return HttpResponse("<h1>Believe in today's hardwork..</h1>")
def Html_2(request):
    return render(request,'style2.html')
