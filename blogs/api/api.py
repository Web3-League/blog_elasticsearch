from django.urls import include, path



urlpatterns = [
    path('blog/',include('blogs.blog.blogs')),
    path('media/', include('blogs.media.media')),
    path('comments/', include('blogs.comment.comment')),
    path('search/', include('blogs.search.search')),
    path('categories/', include('blogs.categories.categories')),
    path('authors/', include('blogs.authors.authors')),
    path('post/', include('blogs.post.post')),

    # Autres URLs pour d'autres vues API
]
