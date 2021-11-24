# step 2.2: create 3 function with pass
# step 3.5: render the index page an include the path 


from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')

def post(request):
    return render(request, 'blog/all-posts.html')

def post_Details(request):
    pass