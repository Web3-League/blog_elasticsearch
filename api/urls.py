from django.urls import include, path



app_name = 'api'
# Préfixe toutes les URLs avec '/api/'

urlpatterns = [
    path('blogs/', include('blogs.api.api')),
    path('robot_gestion/', include('robot.api.api')),
    path('oauth/', include('oauth.oauth')),
    path('web3/', include('web_eth.api_eth.urls')),
]
