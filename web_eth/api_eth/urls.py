from django.urls import include, path

app_name = 'web3'
urlpatterns = [
    path('wallets/', include('web_eth.finance.finance')),
]