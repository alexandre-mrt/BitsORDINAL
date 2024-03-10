import requests
import json

# Set the URL for the API endpoint
url = "https://open-api.unisat.io/v2/inscribe/order/create"

# Replace these with the actual values you want to send
'''
const address = ''; // the receiver address
const inscriptionBalance = 546; // the balance in each inscription
const fileCount = 1000; // the fileCount
const fileSize = 1000; // the total size of all files
const contentTypeSize = 100; // the size of contentType
const feeRate = 10; // the feeRate
const feeFileSize = 100; // the total size of first 25 files
const feeFileCount = 25 // do not change this
const devFee = 1000; // the fee for developer

const balance = inscriptionBalance * fileCount;

let addrSize = 25+1; // p2pkh
if(address.indexOf('bc1q')==0 || address.indexOf('tb1q')==0){
    addrSize = 22+1;
}else if(address.indexOf('bc1p')==0 || address.indexOf('tb1p')==0){
    addrSize = 34+1;
}else if(address.indexOf('2')==0 || address.indexOf('3')==0){
    addrSize = 23+1;
}

const baseSize = 88;
let networkSats = Math.ceil(((fileSize+contentTypeSize) / 4 + ( baseSize+8+addrSize+8+23)) * feeRate);
if(fileCount>1){
    networkSats = Math.ceil(((fileSize+contentTypeSize) / 4 + (baseSize+8+addrSize+(35+8)*(fileCount-1)+ 8+23 +(baseSize+8+addrSize+0.5)*(fileCount-1) )) * feeRate);
}
let networkSatsByFeeCount = Math.ceil(((feeFileSize+contentTypeSize) / 4 + ( baseSize+8+addrSize+8+23)) * feeRate);
if(fileCount>1){
    networkSatsByFeeCount = Math.ceil(((( feeFileSize)+contentTypeSize*(feeFileCount/fileCount)) / 4 + (baseSize+8+addrSize+(35+8)*(fileCount-1)+ 8+23 +(baseSize+8+addrSize+0.5)*Math.min(fileCount-1,feeFileCount-1) )) * feeRate);
}

const baseFee = 1999 * Math.min(fileCount, feeFileCount); // 1999 base fee for top 25 files
const floatFee = Math.ceil(networkSatsByFeeCount * 0.0499); // 4.99% extra miner fee for top 25 transations
const serviceFee = Math.floor(baseFee + floatFee);

const total = balance + networkSats + serviceFee; 
const truncatedTotal = Math.floor((total) / 1000) * 1000; // truncate
const amount = truncatedTotal + devFee; // add devFee at the end

console.log("The final amount need to pay: ",amount)
'''
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