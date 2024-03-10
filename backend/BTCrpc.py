import requests

# Constants for URL endpoints and block information
BLOCKCHAIN_INFO_ADDRESS_URL = 'https://blockchain.info/rawaddr/'
BLOCKCHAIN_INFO_TX_URL = 'https://blockchain.info/rawtx/'
GENESIS_BLOCK_YEAR = 2009
CURRENT_YEAR = 2024
PAGE_SIZE = 50  # The API returns a maximum of 50 transactions per page

def get_transaction_count(bitcoin_address):
    """
    Retrieves the total transaction count for a given Bitcoin address.
    """
    url = f'{BLOCKCHAIN_INFO_ADDRESS_URL}{bitcoin_address}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['n_tx']
    else:
        print('Failed to retrieve data:', response.status_code)
        return None

def get_oldest_transaction_hash(bitcoin_address, transaction_count):
    """
    Retrieves the hash of the oldest transaction for a given Bitcoin address.
    """
    pages = (transaction_count + PAGE_SIZE - 1) // PAGE_SIZE  # Calculate total pages
    final_page_offset = (pages - 1) * PAGE_SIZE  # Calculate offset for the last page
    url = f'{BLOCKCHAIN_INFO_ADDRESS_URL}{bitcoin_address}?offset={final_page_offset}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'txs' in data and data['txs']:
            oldest_transaction = data['txs'][-1]  # Get the last transaction
            return oldest_transaction['hash']
    else:
        print('Failed to retrieve data:', response.status_code)
        return None

def get_oldest_transaction_info(bitcoin_address):
    """
    Returns the oldest transaction of the user, with the block height and the number of transactions.
    """
    transaction_count = get_transaction_count(bitcoin_address)

    if transaction_count is not None:
        print(f'The address {bitcoin_address} has {transaction_count} transactions.')
        oldest_transaction_hash = get_oldest_transaction_hash(bitcoin_address, transaction_count)

        if oldest_transaction_hash:
            print(f'The oldest transaction hash is: {oldest_transaction_hash}')
            tx_url = f'{BLOCKCHAIN_INFO_TX_URL}{oldest_transaction_hash}'
            tx_response = requests.get(tx_url)
            if tx_response.status_code == 200:
                tx_data = tx_response.json()
                block_height = tx_data['block_height']
                print(f"Block height for the oldest transaction: {block_height}")
                
                block_time_estimation = GENESIS_BLOCK_YEAR + (block_height / (6 * 24 * 365.25))
                print(f"Estimated year of the oldest transaction: {int(block_time_estimation)}")
                return block_time_estimation, transaction_count
            else:
                print('Failed to retrieve transaction data:', tx_response.status_code)
        else:
            print('Could not retrieve the oldest transaction hash.')
    else:
        print('Could not retrieve the transaction count.')

    return None, 0

