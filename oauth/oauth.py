from django.urls import path
from . import views

urlpatterns = [
    path('oauth/authorize/', views.token, name='oauth-authorize'),
    path('oauth/refresh/', views.refresh_token, name='oauth-refresh'),
    path('oauth/revoke/', views.revoke_token, name='oauth-revoke'),
]
