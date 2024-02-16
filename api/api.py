from django.urls import include, path



app_name = 'api'
# Préfixe toutes les URLs avec '/api/'
urlpatterns = [
    path('blog/',include('blog.blogs')),
    path('media/', include('media.media')),
    path('comments/', include('comment.comment')),
    path('search/', include('search.search')),
    path('categories/', include('categories.categories')),
    path('authors/', include('authors.authors')),
    path('post/', include('post.post')),

    # Autres URLs pour d'autres vues API
]
