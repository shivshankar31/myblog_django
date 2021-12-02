from django.contrib import admin

# step 16.1: register all three models in admin.py file to access the models on admin panel.
# step 16.2: also add admin panel display class and add to register.



from blog.models import Author, Post, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'excerpt', 'image_name', 'date', 'slug', 'content')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)


admin.site.register(Post,PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)