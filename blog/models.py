# step 13.1: add models Post in models.py file, with title, excerpt, image_name, date, slug, content.
# Step 14.1: Add Author model in models.py with fields first_name, last_name, email
# step 14.2: add author field in Post as models.foreignkey, it is used to mention (many to one relationship) field.
# step 15.1: add Tag model in models.py with field caption.
# step 15.2: add tags field to Post as models.manytomanyfield.


from django.db import models
from django.db.models.base import Model
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_NULL

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique = True)
    content = models.TextField(validators= [MinLengthValidator(0)])
    author = models.ForeignKey(Author, null= True, on_delete=models.SET_NULL, related_name='Post')
    tags = models.ManyToManyField(Tag)




