import requests
import time

API_ENDPOINT = "https://blockstream.info/api"

# define a function to get all transactions for a given wallet
def get_address_transactions(address: str):
    resp = requests.get(f"{API_ENDPOINT}/address/{address}/txs", timeout=20)
    resp.raise_for_status()
    return resp.json()

# define a function that gets information on a specfic transaction
def get_transaction(transaction_id: str):
    resp = requests.get(f"{API_ENDPOINT}/tx/{transaction_id}", timeout=20)
    resp.raise_for_status()
    return resp.json()

address = "1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX"
transactions = get_address_transactions(address)

for transaction in transactions:
    transaction_id = transaction["txid"]
    print(transaction_id)
    full_transaction = get_transaction(transaction_id)
    print(full_transaction)
    time.sleep(0.2)
