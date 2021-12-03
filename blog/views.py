# step 2.2: create 3 function with pass
# step 3.5: render the index page an include the path 
# step 8.3: add return for detail_post function, also add slug as a argument inorder to view the page
# step 10.1: add recent 3 post on the home page, from dummy data, also images are added
# step 11.1: for all post page function is defind in views.py, to collect all post we use dict in render return  
# step 11.3: In views.py, detail_post function use python next() function to return next item using for and if statements and return a key value
# step 19.1: in view.py file - home page use objects.all and order by decending and slice to get new post
# step 19.2: in view.py file - all post page, same as above use all() to display all post. 
# step 19.3: in view.py file - detail post page, use get object 404 to display the single post.
# step 19.5: remove all unused function and date from view.py file
# step 20.1: In views.py, in order to generate the multiple selected collect all the tags in one key - 'post_detail.tags.all()'.

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Tag

# Create your views here.

def home(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', { 'post': latest_post })

def post(request):
    all_post = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {
        'allpost' : all_post
    })

def detail_post(request, slug):
    #method 1
    # post_detail = Post.objects.get(slug = slug) 
    # method 2 
    post_detail = get_object_or_404(Post, slug = slug)

    #identified_post = next(post for post in allposts if post['slug'] == slug)
    return render(request, 'blog/detail_post.html', {
        'post_detail' : post_detail,
        'post_tag' : post_detail.tags.all()
        })