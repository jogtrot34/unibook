from django.urls import path
from .views import home_view, books_view,field_view,course_view
urlpatterns = [
    path('',home_view, name='home' ),
    path('books/', books_view, name='books'),
    path('books/<int:field_id>', field_view, name='field'),
    path('books/fields/<int:course_id>', course_view, name='courses')
]