from django.contrib import admin
from blogs.comment.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog_post', 'content', 'created_at', 'blog_post')
    search_fields = ['blog_post__title', 'content']
    list_filter = ('blog_post',)




