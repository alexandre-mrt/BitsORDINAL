<<<<<<< HEAD
from bitcoinlib.wallets import Wallet, wallet_create_or_open
from bitcoinlib.transactions import Transaction, Output
=======
import bitcoinlib
import bitcoinlib.networks as networks
from bitcoinlib.wallets import wallet_create_or_open
>>>>>>> 9cbd29c0a36048d6aa19b63b0593c8db4333ce09
from flask import Flask, request, jsonify
import os

# Environment variable for the private key
<<<<<<< HEAD
private_key = "cTYhgHA7fxH7ziZsxyKiLctZDoznzQEgsa5QWpQQ5cM875jxV76z"
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


# Need to get as a parameter the address to send the funds to
=======
network = 'testnet'

wallet = wallet_create_or_open("Sponsorising", network= network, witness_type='P2TR')
print(wallet.scan())
print(wallet.info())

private_key = wallet.get_key()
print("wifazepzajeozairjhazoirazoraz")
print(wallet.wif())
account = wallet.new_account("Sponsor")


app = Flask(__name__)

>>>>>>> 9cbd29c0a36048d6aa19b63b0593c8db4333ce09
@app.route('/mint', methods=['POST'])
def mint():
    data = request.get_json()
    user_address = data.get('user_address')
    amount = data.get('amount')
<<<<<<< HEAD
    
=======

>>>>>>> 9cbd29c0a36048d6aa19b63b0593c8db4333ce09
    if not user_address or not amount:
        return jsonify({"status": "error", "message": "Invalid user address or amount"}), 400

    try:
        # Initialize wallet
<<<<<<< HEAD
        wallet = wallet_create_or_open("SponsoredWallet", keys=private_key, network=network)

        # Create, sign, and broadcast the transaction
        tx = create_transaction(wallet, user_address, amount)
        signed_tx = sign_transaction(wallet, tx)
        txid = broadcast_transaction(wallet, signed_tx)
        
=======
        print(wallet.scan())
        print(wallet.info())
        print(wallet.get_key())

        # Create, sign, and send the transaction in one step
        # Replace `send_to` with the actual function name and its required parameters
        txid = wallet.send_to(user_address, amount, network = network)

>>>>>>> 9cbd29c0a36048d6aa19b63b0593c8db4333ce09
        return jsonify({"status": "success", "transaction_id": txid}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
