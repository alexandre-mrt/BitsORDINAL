import requests

# Mint an inscription. Take care to send the file fast enough to avoid the mint_id to expire
url = "https://api-testnet.deezy.io/v1/inscriptions/mint"
receive_address = "tb1pr772wm3jdlkdf7jez703ahpxztgd0vgeqdjpwm3am2q6uzwkdwdqcc6a5u"

payload = {
  "file_data_base64": "PHVzZXJfbmFtZT4gOyA8Zmlyc3RfdHJhbnNhYz4=",
  "file_extension": "text",
  "on_chain_fee_rate": 5,
  "receive_address": "tb1pr772wm3jdlkdf7jez703ahpxztgd0vgeqdjpwm3am2q6uzwkdwdqcc6a5u",
  "cursed": False
}


headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)

#"prev mint_id = f6151c6208ed6a4212f22434e5085c0f"

# Get the mint status


url = "https://api-testnet.deezy.io/v1/inscriptions/mint"

query = {
  "mint_id": "c1af8d35e84060581ac254cc83d68be7"
}

response = requests.get(url, params=query)

data = response.json()
print(data)


{
"mint_attempt_id": "8bbc0e3a72d4b05746bc635ce7a6ddda",
"bolt11_invoice": "lntb117920n1pj76p4gpp59wh4yw2wc7wqm4g6dd5whtw8l0pm89e64maa97u4zhemqfjyhpzsdp4f45kuapqxysyxatnw3hk6gzdd9h8ggrxdaezqvf3xuunygrnv968xcqzzsxqzrcsp5glqqupv6z3txfh6p52adqjtwqtgw8fpskq49rdyzh2mhtz4vupms9qyyssqu5nujt74v8chywxg976wmha3t65rh9rjsxmj6v29u6ah0pr6l89ygk8h5gd0kmucenjjl8tkvnu28d56fsp5jkjx79p38u6k7axwufcp0c5fls",
"payment_address": "tb1q87erepnqyjn24l5pz78nyt85g8pa6t4ul82f04",
"amount_sats": 11792,
"file_size_in_bytes": 8
}
