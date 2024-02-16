import os
import ssl
from nftback.settings import BASE_DIR
from elasticsearch import Elasticsearch


ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
ca_certs_path = os.path.join(BASE_DIR,'elasticsearch-8.12.1/config/certs/http_ca.crt')

client = Elasticsearch("https://192.168.1.16:9200/",
                        http_auth=("elastic", "g-weCrKp+4ysP-_whcMQ"),
                        verify_certs=False,  # Disable certificate verification (equivalent to --insecure option)
                        ca_certs=ca_certs_path
                        )

# elasticsearch.py



def index_blogpost(sender,instance,created, **kwargs):
    media_path = instance.media.path if instance.media else None

    client.index(index='search-blog_core', id=instance.id, body={
        'title': instance.title,
        'content': instance.content,
        'created_at': instance.created_at.isoformat(),
        'media': media_path,
        'categories': [categorie.nom for categorie in instance.categories.all()],
        'authors': [author.nom for author in instance.authors.all()],
        # Add more fields as needed

    })

def delete_blogpost(sender, instance, **kwargs):
    client.delete(index='search-blog_core', id=instance.id)



def update_blogpost(sender, instance, **kwargs):
    media_path = instance.media.path if instance.media else None
    client.update(index='search-blog_core', id=instance.id, body={
        'doc': {
            'title': instance.title,
            'content': instance.content,
            'created_at': instance.created_at.isoformat(),
            'media': media_path,
            'categories': [categorie.nom for categorie in instance.categories.all()],
            'authors': [author.nom for author in instance.authors.all()],
            # Add more fields as needed
        }
    })

def read_blogpost(sender, instance, **kwargs):
    client.get(index='search-blog_core', id=instance.id)

