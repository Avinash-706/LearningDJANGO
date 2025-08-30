from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def front(request):
    return HttpResponse("Hey I am a DJ") 

def success_page(request):
    b = '*'*10
    a = f"<h1> {b} <h1>"

    return HttpResponse(a + "<h3>SUCCESS !!<h3>")