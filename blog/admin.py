from django.contrib import admin

# step 16.1: register all three models in admin.py file to access the models on admin panel.
# step 16.2: also add admin panel display class and add to register.
# step 18.1: To create slug automaticly, add 'prepopulated_fields = {'slug': ('title',)}' field in admin.py 
# step 31.1: adding comment to admin.py admin.site.register



from blog.models import Author, Comment, Post, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','image', 'slug', 'date')
    prepopulated_fields = {'slug': ('title',)} 

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post', 'email', 'text', 'date')

admin.site.register(Post,PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)