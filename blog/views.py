# step 2.2: create 3 function with pass
# step 3.5: render the index page an include the path 
# step 8.3: add return for detail_post function, also add slug as a argument inorder to view the page


from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')

def post(request):
    return render(request, 'blog/all-posts.html')

def detail_post(request, slug):
    return render(request, 'blog/detail_post.html')