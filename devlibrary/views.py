from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from comments.forms import CommentForm
from comments.models import Comment
from devlibrary.models import Library


@login_required
def library_rating(request, id):
    context = {}
    return render(request, "confirm_delete.html", context)


def libraries_list(request):
    list = Library.objects.all()
    paginator = Paginator(list, 3)
    page = request.GET.get('page')  # Show 25 contacts per page
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, "list.html", {"libraries": list})


@login_required
def library(request):
    list = library.objects.all()
    page = request.GET.get('page', 1)  # Show 25 contacts per page
    paginator = Paginator(list, 1)

    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list = paginator.page(paginator.num_pages)
    return render(request, "dummy.html", {"list": list})


def librarydetail(request, id):
    devLib = get_object_or_404(Library, id=id)
    comments = Comment.objects.filter(library_id=id)
    # logic for saving form
    form = CommentForm(request.POST or None)
    #print(form)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        #Library.objects.filter(pk=devLib.pk).update(comments=devLib.comments + 1)
        return HttpResponseRedirect(devLib.get_absolute_url())

    context = {
        "library": devLib,
        "comments": comments,
        "comment_form": form,
    }
    return render(request, "lib_details.html", context)
