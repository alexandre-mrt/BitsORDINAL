import requests
import json

# Set the URL for the API endpoint
url = "https://open-api.unisat.io/v2/inscribe/order/create"

# Replace these with the actual values you want to send

# Will make a call to the front to get the connected addres
#TODO
receive_address = "your_receive_address_here"
dev_address = "02eeeab1bb5023e1e127efe565cd5aa92a4f9d339bd335abdcf3ee36c37df2c0b7"
data_url = "https://i0.wp.com/crncy.com.au/wp-content/uploads/Screenshot-2024-03-07-at-6.07.10-pm.png?w=1066&ssl=1" # This should be a base64 encoded string

# Create the data payload as a dictionary
data = {
    "receiveAddress": receive_address,
    "feeRate": 1,
    "outputValue": 546,
    "files": [
        {
            "username": "BitsOjizz",
            "origin_account": receive_address,
            "block_height": 1,
            "dataURL": data_url
        }
    ],
    "devAddress": dev_address,
    "devFee": 0
}

# Set the correct headers for a JSON post request
headers = {
    'Content-Type': 'application/json'
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    print("Order created successfully.")
    print(response.json())  # Assuming the API returns JSON data
else:
    print("Failed to create order. Status code:", response.status_code)
    print("Response:", response.text)