from django.db import models

# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='field')

    def __str__(self):
        return f"{self.name}--{self.field.name}"

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='book_field', null=True, blank=False)
    cover = models.ImageField(upload_to='covers/', default='covers/default.png')
    file = models.FileField(upload_to='books/', null=False, blank=False)

    def __str__(self):
        return f'({self.course}){self.author}: {self.name}'