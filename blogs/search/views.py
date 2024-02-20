from django.http import JsonResponse
from nftback.elasticsearch import client


def generer_requete(contenu):
    if "media:" in contenu:
        return contenu
    elif contenu:
        fields = ["title", "content", "name", "authors", "description", "tags", "category","media", "author", "column1", "column2", "column3", "Mot", "Def" ]
        queries = [f"{field}:{contenu}" for field in fields]
        wildcard_queries = [f"{field}:*{contenu}*" for field in fields]
        return " OR ".join(queries + wildcard_queries)
    else:
        return "*:*"



def search_view(request,query):

    contenu_recherche = query
    requete_generique = generer_requete(contenu_recherche)

    # Exécuter la recherche dans Elasticsearch
    if contenu_recherche:
        # Rechercher dans les champs "name" et "author"
        #results = client.search(index="search-blog_core", q=requete_generique)
        dict_result = client.search(index="search-dictionary,search-blog_core,search-dico_fr", q=requete_generique)
    else:
        # Recherchez tous les documents si aucun terme de recherche n'est spécifié
        #results = client.search(index="search-blog_core", q="*:*")
        
        dict_result = client.search(index="dictionary,search-dictionary,search-dico_fr", q="*:*")

    results_list = []
    for hit in dict_result['hits']['hits']:
        result_dict = {
            'pos': hit['_source'].get('column2', ''),
            'word': hit['_source'].get('column1', ''),
            'definition': hit['_source'].get('column3', ''),
            'mot': hit['_source'].get('Mot', ''),
            'def': hit['_source'].get('Def', ''),
            'name': hit['_source'].get('name', ''),
            'author': hit['_source'].get('authors', ''),
            'authors': hit['_source'].get('author', ''),
            'release_date': hit['_source'].get('release_date', ''),
            'page_count': hit['_source'].get('page_count', ''),
            'title': hit['_source'].get('title', ''),
            'content': hit['_source'].get('content', ''),
            'created_at': hit['_source'].get('created_at', ''),
            'media': hit['_source'].get('media', ''),
            'category': hit['_source'].get('categories', ''),
            'tags': hit['_source'].get('tags', ''),
            'description': hit['_source'].get('description', ''),

            }
        
        results_list.append(result_dict)

    return JsonResponse({'results': results_list}, safe=False)
"""
    # Construire une liste de résultats
    results_list = []
    for hit in results['hits']['hits']:
        result_dict = {
            'name': hit['_source'].get('name', ''),
            'author': hit['_source'].get('authors', ''),
            'authors': hit['_source'].get('author', ''),
            'release_date': hit['_source'].get('release_date', ''),
            'page_count': hit['_source'].get('page_count', ''),
            'title': hit['_source'].get('title', ''),
            'content': hit['_source'].get('content', ''),
            'created_at': hit['_source'].get('created_at', ''),
            'media': hit['_source'].get('media', ''),
            'category': hit['_source'].get('categories', ''),
            'tags': hit['_source'].get('tags', ''),
            'description': hit['_source'].get('description', ''),
        }

        results_list.append(result_dict)

"""


####

