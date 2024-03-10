import bitcoinlib
import bitcoinlib.networks as networks
from bitcoinlib.wallets import wallet_create_or_open
from flask import Flask, request, jsonify
import os
import satApi 

# Environment variable for the private key
network = 'testnet'

wallet = wallet_create_or_open("Bitso", network= network, witness_type='segwit')
print(wallet.scan())
print(wallet.info())

private_key = wallet.get_key()
#print("wifazepzajeozairjhazoirazoraz")
#print(wallet.wif())
account = wallet.new_account("Sponsor")


app = Flask(__name__)

@app.route('/mint', methods=['POST'])
def mint():
    data = request.get_json()
    user_address = data.get('user_address')
    amount = data.get('amount')

    if not user_address or not amount:
        return jsonify({"status": "error", "message": "Invalid user address or amount"}), 400

    try:
        tx = wallet.send_to(user_address, amount, network=network, offline=False)
        print(tx)
        wallet.scan()
        #t = wallet.sweep(user_address, network = network)
        print(t)
        # Extract relevant transaction information
        print(t.outputs)
        tx_data = {
            "txid": tx.txid,
            "amount": amount,
            "user_address": user_address
        }
        return jsonify({"status": "success", "transaction": tx_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
