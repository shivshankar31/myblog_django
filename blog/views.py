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
# step 23.1: In views.py, convert all function to class based view
# step 25.3: In views.py, import created form class, in detailPost class under get context data function call the created CommentForm and name it
# step 27.2: In views.py, insted of DetailView, use View and manually create get and post function 
# step 29.1: In views.py, as we give the name in comment model, call that in detail



from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import View
from blog.models import Post, Tag
from django.views.generic import ListView, DetailView
from .forms import CommentForm
# Create your views here.


class HomeView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'post'
    ordering = ['-date']

    def get_queryset(self):
        query =  super().get_queryset()
        data = query[:3]
        return data


# def home(request):
#     latest_post = Post.objects.all().order_by("-date")[:3]
#     return render(request, 'blog/index.html', { 'post': latest_post })

class PostList(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'allpost'
  

# def post(request):
#     all_post = Post.objects.all().order_by('-date')
#     return render(request, 'blog/all-posts.html', {
#         'allpost' : all_post
#     })


class DetailPost(View):

    def get(self, request, slug):
        post = Post.objects.get(slug = slug)
        details = {
            'post_detail': post,
            'post_tag': post.tags.all(),
            'comment_form': CommentForm(),
            'comment': post.comments.all().order_by('-id')
        }
        return render(request, 'blog/detail_post.html', details)


    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug = slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('blog_details', args=[slug]))

        
        # details = {
        #     'post': post,
        #     'post_tag': post.tags.all(),
        #     'comment_form': comment_form
        # }
        return render(request, 'blog/detail_post.html', {
            'post_detail': post,
            'post_tag': post.tags.all(),
            'comment_form': comment_form,
            'comment': post.comments.all().order_by('-id')
        } )

        


# class DetailPost(DetailView):
#     template_name = 'blog/detail_post.html'
#     model = Post
#     context_object_name = 'post_detail'

#     def get_context_data(self, **kwargs):
#         context1 = super().get_context_data(**kwargs)
#         context1['post_tag'] = self.object.tags.all()
#         context1['comment_form'] = CommentForm()
#         return context1 

   
# def detail_post(request, slug):
#     #method 1
#     # post_detail = Post.objects.get(slug = slug) 
#     # method 2 
#     post_detail = get_object_or_404(Post, slug = slug)

#     #identified_post = next(post for post in allposts if post['slug'] == slug)
#     return render(request, 'blog/detail_post.html', {
#         'post_detail' : post_detail,
#         'post_tag' : post_detail.tags.all()
#         })