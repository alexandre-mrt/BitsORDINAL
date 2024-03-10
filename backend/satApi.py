import requests
import json
from math import ceil, floor
import bitcoinlib
from bitcoinlib.wallets import Wallet
from flask import Flask, request, jsonify

# Constants
NETWORK = 'testnet'
WALLET_NAME = "Bitso"
WITNESS_TYPE = 'segwit'
API_URL = "https://open-api.unisat.io/v2/inscribe/order/create"

# Create and open wallet
wallet = bitcoinlib.wallets.wallet_create_or_open(WALLET_NAME, network=NETWORK, witness_type=WITNESS_TYPE)
sponsorAddress = wallet.get_key().address

app = Flask(__name__)

def calculateFees(sponsor):
    """
    Calculate the fees required for a transaction.
    """
    address = sponsor
    inscription_balance = 546
    file_count = 1
    file_size = 100
    content_type_size = 100
    fee_rate = 10
    fee_file_size = 100
    fee_file_count = 25
    dev_fee = 1000

    balance = inscription_balance * file_count
    addr_size = 26  # default p2pkh size

    if address.startswith('bc1q') or address.startswith('tb1q'):
        addr_size = 23
    elif address.startswith('bc1p') or address.startswith('tb1p'):
        addr_size = 35
    elif address.startswith('2') or address.startswith('3'):
        addr_size = 24

    base_size = 88
    network_sats = calculateNetworkSats(file_size, content_type_size, addr_size, base_size, file_count, fee_rate)
    network_sats_by_fee_count = calculateNetworkSats(fee_file_size, content_type_size, addr_size, base_size, file_count, fee_rate, fee_file_count)

    base_fee = 1999 * min(file_count, fee_file_count)
    float_fee = ceil(network_sats_by_fee_count * 0.0499)
    service_fee = floor(base_fee + float_fee)

    total = balance + network_sats + service_fee
    truncated_total = floor(total / 1000) * 1000
    amount = truncated_total + dev_fee

    print("The final amount need to pay: ", amount)
    return amount

def calculateNetworkSats(size, content_size, addr_size, base_size, count, rate, fee_count=None):
    """
    Helper function to calculate network sats.
    """
    if fee_count is None:
        fee_count = count

    network_sats = ((size + content_size) / 4 + (base_size + 8 + addr_size + 8 + 23)) * rate
    if count > 1:
        network_sats = (((size) + content_size * (fee_count / count)) / 4 + (base_size + 8 + addr_size + (35 + 8) * (count - 1) + 8 + 23 + (base_size + 8 + addr_size + 0.5) * min(count - 1, fee_count - 1))) * rate

    return ceil(network_sats)

def mintOGest(customerAddress, username, sponsor):
    """
    Create an order and get the pay address and amount to pay.
    """
    data = {
        "receiveAddress": customerAddress,
        "feeRate": calculateFees(sponsor),
        "outputValue": 546,
        "files": [{"username": username, "origin_account": customerAddress, "date": 1}],
        "devAddress": sponsor,
        "devFee": 0
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        return response_data['data']['payAddress'], response_data['data']['amount']
    else:
        print(f"Failed to create order. Status code: {response.status_code}, Response: {response.text}")
        return None, 0

@app.route('/mint', methods=['POST'])
def mint():
    """
    Endpoint to handle minting requests.
    """
    data = request.get_json()
    
    customer_address = data.get('customer_address')
    name = data.get('name')

    if not customer_address or not name:
        return jsonify({"status": "error", "message": "Invalid address or name"}), 400

    #pay_address, amount = mintOGest(customer_address, name, sponsorAddress) Imagine the API is working 
    pay_address = "tb1q3m9hl0l2k6nn76gygaczuzcq72dapx6rjzy9jr"
    amount = 10000 # in sats

    if not pay_address:
        return jsonify({"status": "error", "message": "Failed to create order"}), 500

    try:
        tx = wallet.send_to(pay_address, amount, network=NETWORK)
        wallet.scan()
        return jsonify({"status": "success", "transaction": {"txid": tx.txid, "amount": amount, "pay_address": pay_address}}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host = 'localhost', port = 9000)
