from django.db import models
from blogs.media.models import Media
from blogs.categories.models import Categorie
from blogs.authors.models import Author
from django.dispatch import receiver
from elasticsearch import Elasticsearch
from django.db.models.signals import post_save, post_delete, m2m_changed
from nftback.elasticsearch import index_blogpost, delete_blogpost, update_blogpost


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Categorie)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
    


@receiver(post_save, sender=BlogPost)
def create_blogpost(sender, instance, created, **kwargs):
    if created:
        index_blogpost(sender, instance, created, **kwargs)
    else:
        update_blogpost(sender, instance, **kwargs)

@receiver(post_delete, sender=BlogPost)
def clear_blogpost(sender, instance, **kwargs):
    delete_blogpost(sender, instance, **kwargs)


@receiver(m2m_changed, sender=BlogPost.categories.through)
@receiver(m2m_changed, sender=BlogPost.authors.through)
def handle_blogpost_m2m_change(sender, instance, action, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        update_blogpost(sender, instance, **kwargs)