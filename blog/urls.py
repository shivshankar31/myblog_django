# step 2.1: create urlpattens using path 
# step 2.3: import views and assign view.function name to call the function inside urlpattens
# step 2.4: assign name for each url path.
# step 23.2: In urls.py, change the path according to class dased views


from django.urls import path
from .import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blogs', views.PostList.as_view(), name='blogs'),
    # path('blogs', views.post, name='blogs'),
    path('blogs/<slug:slug>', views.DetailPost.as_view(), name='blog_details')
]
