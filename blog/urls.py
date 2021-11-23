# step 2.1: create urlpattens using path 
# step 2.3: import views and assign view.function name to call the function inside urlpattens
# step 2.4: assign name for each url path.

from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blogs', views.post, name='blogs'),
    path('blogs/<slug:slug>', views.post_Details, name='blog_details')
]
