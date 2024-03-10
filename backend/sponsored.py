import bitcoinlib
import bitcoinlib.networks as networks
from bitcoinlib.wallets import wallet_create_or_open
from flask import Flask, request, jsonify
import os

# Environment variable for the private key
network = 'testnet'

wallet = wallet_create_or_open("Sponsorising", network= network)
print(wallet.scan())
print(wallet.info())

private_key = wallet.get_key()
print(wallet.get_key())


app = Flask(__name__)

@app.route('/mint', methods=['POST'])
def mint():
    data = request.get_json()
    user_address = data.get('user_address')
    amount = data.get('amount')

    if not user_address or not amount:
        return jsonify({"status": "error", "message": "Invalid user address or amount"}), 400

    try:
        # Initialize wallet
        print(wallet.scan())
        print(wallet.info())
        print(wallet.get_key())

        # Create, sign, and send the transaction in one step
        # Replace `send_to` with the actual function name and its required parameters
        txid = wallet.send_to(user_address, amount)

        return jsonify({"status": "success", "transaction_id": txid}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
