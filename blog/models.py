# step 13.1: add models Post in models.py file, with title, excerpt, image_name, date, slug, content.
# Step 14.1: Add Author model in models.py with fields first_name, last_name, email
# step 14.2: add author field in Post as models.foreignkey, it is used to mention (many to one relationship) field.
# step 15.1: add Tag model in models.py with field caption.
# step 15.2: add tags field to Post as models.manytomanyfield.
# step 24.1: add new comment class in the model and add fields as user_name, email, comment post as models.foreignkey
# step 31.2: to return object into string, redefine __str__ 

from django.db import models
from django.db.models.base import Model
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_NULL

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.caption}'

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    # image_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Prof_img', null = True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique = True)
    content = models.TextField(validators= [MinLengthValidator(0)])
    author = models.ForeignKey(Author, null= True, on_delete=models.SET_NULL, related_name='Post')
    tags = models.ManyToManyField(Tag)

    # if we need to combain two fields then we can use additional function
    # def title1(self):
    #     return f'{self.title}'

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date = models.DateField(auto_now=True, auto_now_add=False)

