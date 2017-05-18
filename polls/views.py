from unicodedata import category

from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.template import loader

from comments.forms import CommentForm
from comments.models import Comment
from devlibrary.models import Library
from polls.models import post


# Create your views here.
def home(request):
    posts = post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def index(request):
    posts = post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def aboutteam(request):
    posts = post.objects.all()
    return render(request, 'about.html', {})


@login_required(login_url="login")
def newhome(request):
    return render(request, 'home.html')


@login_required(login_url="login")
def search_view(request):
    context = {}
    if request.method == 'GET':
        searchText = request.GET.get('q')
        results = Library.objects.filter(name__icontains=searchText)
        count = results.count()

        if count>0:
            context['results'] = results
        else:
            context['msg']="No results found"
        print(context)
    return render(request, 'search.html', context)
