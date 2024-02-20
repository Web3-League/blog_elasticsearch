from web3 import Web3
from django.http import JsonResponse

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

def get_eth_balance(request, address):
    if w3.is_connected():
        if w3.is_address(address):
            balance_wei = w3.eth.get_balance(address)
            balance_eth = Web3.from_wei(balance_wei, 'ether')
            return JsonResponse({'address': address, 'balance': str(balance_eth) + ' ETH'})
        else:
            return JsonResponse({'error': 'Invalid Ethereum address'}, status=400)
    else:
        return JsonResponse({'error': 'Unable to connect to the Ethereum node'}, status=500)


def get_latest_transaction(request, address):

    # Check if the address is valid
    if not w3.is_address(address):
        return JsonResponse({'error': 'Invalid address'}, status=400)

    address = w3.to_checksum_address(address)
    latest = w3.eth.block_number
    transaction_found = None

    # Define the range of blocks you want to scan
    # Note: For performance reasons, this is limited to the last 100 blocks in this example.
    # Adjust according to your needs.
    block_range = 100
    start_block = max(0, latest - block_range)

    for block_number in range(latest, start_block, -1):
        block = w3.eth.get_block(block_number, full_transactions=True)
        for txn in block.transactions:
            if txn['from'] == address or txn.get('to') == address:  # 'to' can be None for contract creations
                transaction_found = txn
                break
        if transaction_found:
            break

    if not transaction_found:
        return JsonResponse({'message': 'No transactions found for this address in the last 100 blocks'})

    # Simplify the response for demonstration
    response = {
        'blockNumber': transaction_found.block_number,
        'hash': transaction_found.hash.hex(),
        'from': transaction_found['from'],
        'to': transaction_found.get('to'),  # 'to' can be None for contract creations
        'value': transaction_found['value'],
        'gas': transaction_found['gas'],
        'gasPrice': transaction_found['gasPrice'],
    }

    return JsonResponse(response)  


