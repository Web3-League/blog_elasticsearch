from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.timezone import now
from django.utils import timezone
from .models import OAuthClient, AccessToken, RefreshToken
import base64
import uuid
import datetime

@csrf_exempt
def token(request):
    if request.method == 'POST':
        auth = request.META.get('HTTP_AUTHORIZATION', None)
        if auth:
            auth_parts = auth.split()
            if len(auth_parts) == 2 and auth_parts[0].lower() == "basic":
                client_id, client_secret = base64.b64decode(auth_parts[1]).decode('utf-8').split(':', 1)
                try:
                    client = OAuthClient.objects.get(client_id=client_id, client_secret=client_secret)
                    # Create a new access token
                    access_token = AccessToken.objects.create(
                        client=client,
                        user=client.user,  # Assuming the token is associated with the client's user
                        token='generate_a_unique_token_here',  # Use a secure method to generate a unique token
                        expires=now() + datetime.timedelta(hours=1)  # Token expires in 1 hour
                    )
                    return JsonResponse({
                        'access_token': access_token.token,
                        'token_type': 'Bearer',
                        'expires_in': 3600,
                    })
                except OAuthClient.DoesNotExist:
                    return JsonResponse({'error': 'invalid_client'}, status=401)
        return JsonResponse({'error': 'invalid_request'}, status=400)
    else:
        return JsonResponse({'error': 'unsupported_method'}, status=405)

@require_POST
def refresh_token(request):
    refresh_token = request.POST.get('refresh_token')
    
    try:
        # Retrieve the refresh token
        refresh_token_obj = RefreshToken.objects.get(token=refresh_token, expires__gt=timezone.now())
        # Generate a new access token
        new_access_token = str(uuid.uuid4())
        expires = timezone.now() + timezone.timedelta(hours=1)  # New token expires in 1 hour
        AccessToken.objects.create(token=new_access_token, client=refresh_token_obj.access_token.client, expires=expires)
        
        # Optionally, you can also update or recreate the refresh token here
        
        return JsonResponse({'access_token': new_access_token, 'expires_in': 3600})
    except RefreshToken.DoesNotExist:
        return JsonResponse({'error': 'Invalid or expired refresh token'}, status=400)

@require_POST
def revoke_token(request):
    token = request.POST.get('token')
    
    # Attempt to revoke access token
    AccessToken.objects.filter(token=token).delete()
    
    # Attempt to revoke refresh token, if applicable
    RefreshToken.objects.filter(token=token).delete()
    
    return JsonResponse({'message': 'Token revoked successfully'})


