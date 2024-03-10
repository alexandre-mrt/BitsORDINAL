import requests

def get_transaction_count(bitcoin_address):
    url = f'https://blockchain.info/rawaddr/{bitcoin_address}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['n_tx']
    else:
        print('Failed to retrieve data:', response.status_code)
        return None

def get_oldest_transaction_hash(bitcoin_address, transaction_count):
    page_size = 50  # The API returns a maximum of 50 transactions per page
    pages = (transaction_count + page_size - 1) // page_size  # Calculate how many pages there are
    final_page_offset = (pages - 1) * page_size  # Calculate the offset for the last page
    url = f'https://blockchain.info/rawaddr/{bitcoin_address}?offset={final_page_offset}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'txs' in data and data['txs']:
            # Assuming transactions are returned in chronological order, the last transaction of the last page is the oldest
            oldest_transaction = data['txs'][-1]  # Get the last transaction
            return oldest_transaction['hash']  # Return the hash of the oldest transaction
    else:
        print('Failed to retrieve data:', response.status_code)
        return None

bitcoin_address = '34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo'
transaction_count = get_transaction_count(bitcoin_address)

oldest_transaction_hash = None
if transaction_count is not None:
    print(f'The address {bitcoin_address} has {transaction_count} transactions.')
    oldest_transaction_hash = get_oldest_transaction_hash(bitcoin_address, transaction_count)
    if oldest_transaction_hash:
        print(f'The oldest transaction hash is: {oldest_transaction_hash}')
else:
    print('Could not retrieve the transaction count or oldest transaction.')

tx_url = f'https://blockchain.info/rawtx/{oldest_transaction_hash}'
tx_response = requests.get(tx_url)
if tx_response.status_code == 200:
            tx_data = tx_response.json()
            # Get the block height
            block_height = tx_data['block_height']
            print(f"Block height for the oldest transaction: {block_height}")
            
            # Calculate the approximate year of the block
            genesis_block_year = 2009
            current_year = 2024
            block_time_estimation = genesis_block_year + (block_height / (6 * 24 * 365.25))
            print(f"Estimated year of the oldest transaction: {int(block_time_estimation)}")
else:
            print('Failed to retrieve transaction data:', tx_response.status_code)
  