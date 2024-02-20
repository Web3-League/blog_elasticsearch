# views.py dans votre application robots
from django.http import JsonResponse
from elasticsearch import Elasticsearch
from nftback.elasticsearch import client as es
import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def robot_list(request):

    robots = es.search(index='search-robots_index', body={'query': {'match_all': {}}})
    return JsonResponse(robots['hits']['hits'], safe=False)

@csrf_exempt
def robot_detail(request, name):
    try:
        # Rechercher le robot par son nom pour obtenir l'ID
        search_response = es.search(index='search-robots_index', body={
            "query": {
                "match_phrase": {
                    "name.keyword": name
                }
            },
            "size": 1
        })

        if search_response['hits']['total']['value'] == 0:
            return JsonResponse({'status': 'error', 'message': 'Robot not found'}, status=404)

        robot = search_response['hits']['hits'][0]

        return JsonResponse(robot, safe=False)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def robot_add(request):
    try:
        data = json.loads(request.body)
        
        # Vérifier si un robot avec le même nom existe déjà
        search_response = es.search(index='search-robots_index', body={
            "query": {
                "match": {
                    "name.keyword": data['name']
                }
            },
            "size": 1
        })

        if search_response['hits']['total']['value'] > 0:
            # Un robot avec le même nom existe déjà
            return JsonResponse({'status': 'error', 'message': 'A robot with this name already exists.'}, status=400)
        
        # Insérer le nouveau robot puisque le nom est unique
        robot = {
            "name": data['name'],
            "description": data['description'],
            "price": data['price'],
            "stock": data['stock']
        }
        es.index(index='search-robots_index', body=robot)
        
        return JsonResponse({'status': 'success', 'message': 'Robot added successfully', 'robot': robot}, status=201)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)



@csrf_exempt
@require_http_methods(["POST"])
def robot_update(request, name):
    try:
        data = json.loads(request.body)

        # Recherche du robot par son nom pour obtenir l'ID
        search_response = es.search(index='search-robots_index', body={
            "query": {
                "match_phrase": {
                    "name.keyword": name  # Assurez-vous que le champ 'name' est correctement configuré dans votre index
                }
            },
            "size": 1
        })

        # Vérifiez si le robot a été trouvé
        if search_response['hits']['total']['value'] == 0:
            return JsonResponse({'status': 'error', 'message': 'Robot not found'}, status=404)

        # Extraire l'ID du robot trouvé
        robot_id = search_response['hits']['hits'][0]['_id']

        # Mise à jour du robot avec l'ID trouvé
        update_response = es.update(
            index='search-robots_index',
            id=robot_id,
            body={"doc": data},  # Mise à jour avec les données fournies
        )

        if update_response['result'] == 'updated':
            return JsonResponse({'status': 'success', 'message': 'Robot updated successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to update robot'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)




@csrf_exempt
@require_http_methods(["DELETE"])  # Utilisation de la méthode HTTP DELETE
def robot_delete(request, name):  
    try:
        # Recherche du robot par son nom pour obtenir l'ID
        search_response = es.search(index='search-robots_index', body={
            "query": {
                "match_phrase": {
                    "name.keyword": name  # Utilisez le champ correct pour le nom
                }
            },
            "size": 1
        })

        # Vérifiez si le robot a été trouvé
        if search_response['hits']['total']['value'] == 0:
            return JsonResponse({'status': 'error', 'message': 'Robot not found'}, status=404)

        # Extraire l'ID du robot trouvé
        robot_id = search_response['hits']['hits'][0]['_id']

        # Suppression du robot avec l'ID trouvé
        response = es.delete(index='search-robots_index', id=robot_id)
        if response.get('result') == 'deleted':
            return JsonResponse({'status': 'success', 'message': 'Robot deleted successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Robot not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def robot_update_location(request, name):
    try:
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # Rechercher le document par nom pour obtenir l'ID
        search_response = es.search(index='search-robots_index', body={
            "query": {
                "match": {
                    "name.keyword": name  # Utilisez name.keyword si name est de type text avec un champ keyword
                }
            }
        })

        # Vérifier si le robot existe
        if search_response['hits']['total']['value'] > 0:
            document_id = search_response['hits']['hits'][0]['_id']
            
            # Mise à jour de la localisation du robot avec l'ID trouvé
            update_response = es.update(
                index='search-robots_index',
                id=document_id,
                body={
                    "doc": {
                        "latitude": latitude,
                        "longitude": longitude
                    }
                }
            )

            # Vérifiez si la mise à jour a été réalisée avec succès
            if update_response['result'] == 'updated':
                return JsonResponse({'status': 'success', 'message': 'Location updated successfully'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Failed to update location'}, status=400)
        else:
            return JsonResponse({'status': 'error', 'message': 'Robot not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


