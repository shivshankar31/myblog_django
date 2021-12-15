# step 25.1: add forms.py file in the add, import model class and forms
# step 25.2: create a class CommentForm and call the model and add or exclude fields form model class and use lables to rename the fields



from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__' #this can be uses to fetch allfields form the model class
        # fields = ['']# also we can list required fields
        exclude = ['post'] #this will exclude the listed fields
        lables = {
            'user_name': 'Your Name',
            'email': 'Email',
            'text': 'Comment'
        }