from bitcoinlib.wallets import Wallet, wallet_create_or_open
from bitcoinlib.transactions import Transaction, Output
from flask import Flask, request, jsonify
import os

# Environment variable for the private key
private_key = os.getenv('SPONSORED_WALLET_PRIVATE_KEY')
network = 'bitcoin'

app = Flask(__name__)

def create_transaction(wallet, recipient_address, amount):
    # Create a new transaction (Not broadcasted yet)
    outputs = [Output(amount, recipient_address, 'btc')]
    return Transaction(wallet, outputs=outputs)

def sign_transaction(wallet, transaction):
    # Sign the transaction with the wallet's private keys
    return wallet.sign_transaction(transaction)

def broadcast_transaction(wallet, transaction):
    # Broadcast the signed transaction to the Bitcoin network
    return wallet.send_raw(transaction)

@app.route('/mint', methods=['POST'])
def mint():
    data = request.get_json()
    user_address = data.get('user_address')
    amount = data.get('amount')
    
    if not user_address or not amount:
        return jsonify({"status": "error", "message": "Invalid user address or amount"}), 400

    try:
        # Initialize wallet
        wallet = wallet_create_or_open("SponsoredWallet", keys=private_key, network=network)

        # Create, sign, and broadcast the transaction
        tx = create_transaction(wallet, user_address, amount)
        signed_tx = sign_transaction(wallet, tx)
        txid = broadcast_transaction(wallet, signed_tx)
        
        return jsonify({"status": "success", "transaction_id": txid}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
