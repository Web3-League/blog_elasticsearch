from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from blogs.blog.models import BlogPost
from .models import Comment
from .forms import CommentForm

def add_comment(request, post_id):
    # Récupérer l'article de blog associé au commentaire
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Créer une nouvelle instance de commentaire associée à l'article de blog
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return JsonResponse({'success': True, 'message': 'Comment added successfully'})
    else:
        form = CommentForm()

    return JsonResponse({'success': False, 'errors': form.errors})

def get_comments(request, post_id):
    # Récupérer tous les commentaires associés à l'article de blog
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()

    # Sérialiser les commentaires en JSON
    comments_json = [{'content': comment.content, 'created_at': comment.created_at} for comment in comments]

    return JsonResponse(comments_json, safe=False)

