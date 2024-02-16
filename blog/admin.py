from django.contrib import admin
from django.http import HttpResponseRedirect
from .models import BlogPost
from comment.models import Comment
from categories.models import Categorie

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    inlines = [CommentInline]  # Ajoute l'inline pour afficher les commentaires
    filter_horizontal = ('categories','authors')

    def add_comment(self, request, queryset):
        # Récupérer l'article de blog sélectionné
        selected_blogpost = queryset.first()

        # Rediriger vers la page d'ajout de commentaire avec l'ID de l'article de blog pré-rempli
        return HttpResponseRedirect(f"/admin/comment/comment/add/?post={selected_blogpost.id}")

    add_comment.short_description = "Add Comment"  # Nom du bouton d'action personnalisée

    actions = ['add_comment']  # Ajoute l'action personnalisée à la liste des actions disponibles

