from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World, Django<h1>")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)-1]
    str = ("title = %s, category = %s, date_time = %s, content = %s" %(post.title, post.category,post.date_time,post.content))
    return HttpResponse(str)