from django.urls import path
from .views import get_eth_balance, get_latest_transaction


urlpatterns = [
    path('balance/<str:address>/', get_eth_balance, name='get_eth_balance'),
    path('history/<str:address>/', get_latest_transaction, name='get_transaction_history'),
]