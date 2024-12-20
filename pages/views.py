from django.shortcuts import render, get_object_or_404, redirect
from .models import Field, Course, Book


# Create your views here.
def home_view(request):

    context ={

    }

    return render(request, 'index.html', context)

def books_view(request):
    fields = Field.objects.all()
    books = Book.objects.all()
    context ={
        'fields':fields,
        'books':books
    }

    return render(request, 'books.html', context)

def field_view(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    courses = Course.objects.filter(field=field)
    books = Book.objects.filter(field= field)
    context ={
        'courses':courses,
        'books':books
    }

    return render(request, 'fields.html', context)

def course_view(request, course_id):
    field = get_object_or_404(Course, pk=course_id)
    fields = Field.objects.all()
    books = Book.objects.filter(course= field)
    context ={
        'fields':fields,
        'books':books
    }

    return render(request, 'courses.html', context)