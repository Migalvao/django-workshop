from django.db import reset_queries
from django.shortcuts import render
from .models import School, Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from datetime import datetime

# Create your views here.


def index(request):

    return render(request, 'index.html')


def schools_view(request):

    schools = School.objects.all()
    context = {"schools": schools}

    return render(request, 'schools.html', context=context)


def single_school_view(request, pk):

    try:
        school = School.objects.get(pk=pk)
    except Exception:
        return render(request, 'school_not_found.html')

    # school = get_object_or_404(School, pk=pk)

    # school = School.objects.filter(pk=pk)
    # if school.exists

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            # criar novo comentario
            author = form.cleaned_data['author']
            text = form.cleaned_data['text']

            # comment = Comment.objects.create(author=author, text=text,
            #                                  school=school, datetime=datetime.now())

            comment = Comment(author=author, text=text,
                              school=school, datetime=datetime.now())

            comment.save()

    comments = Comment.objects.filter(school=pk).order_by('-datetime')
    form = CommentForm()

    context = {"school": school, "comments": comments, "form": form}

    return render(request, 'school.html', context=context)
