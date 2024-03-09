import requests

# Replace 'bitcoin_address' with the actual Bitcoin address you're interested in
bitcoin_address = '34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo'




def get_transaction_count(bitcoin_address):
    # Endpoint URL for the Blockchain Info API
    url = f'https://blockchain.info/rawaddr/{bitcoin_address}'
    
    # Make a GET request to the Blockchain.info API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract and return the number of transactions
        return data['n_tx']
    else:
        print('Failed to retrieve data:', response.status_code)
        return None

# Replace 'bitcoin_address' with the actual Bitcoin address you're interested in
transaction_count = get_transaction_count(bitcoin_address) - 1
print(transaction_count)
 

# Endpoint URL for the Blockchain Info API

if transaction_count is not None:
    print(f'The address {bitcoin_address} has {transaction_count} transactions.')
else:
    print('Could not retrieve the transaction count.')

url = f'https://blockchain.info/rawaddr/{bitcoin_address}?offset={transaction_count}'

# Make a GET request to the Blockchain.info API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Check if there are transactions
    if 'txs' in data:
        # Retrieve the hashes of all transactions
        transaction_hashes = [tx['hash'] for tx in data['txs']]
        # Print each transaction hash
        for hash in transaction_hashes:
            print(hash)
    else:
        print('No transactions found for this address.')
else:
    print('Failed to retrieve data:', response.status_code)


url = "https://blockchain.info/rawtx/{transaction_hash}"
# Make a GET request to the Blockchain.info API
response = requests.get(url)
# get the block height
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Check if there are transactions
    if 'txs' in data:
        # Retrieve the hashes of all transactions
        transaction_hashes = [tx['hash'] for tx in data['txs']]
        # Print each transaction hash
        for hash in transaction_hashes:
            print(hash)

        block_height = data['txs']['block_height']
        print(block_height)
    else:
        print('No transactions found for this address.')
else:
    print('Failed to retrieve data:', response.status_code)