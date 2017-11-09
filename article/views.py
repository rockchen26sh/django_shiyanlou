from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World, Django<h1>")

def detail(request, my_args):
    return HttpResponse("You're looking at my_args %s." % my_args)