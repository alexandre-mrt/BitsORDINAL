from bitcoinlib.wallets import Wallet


# Private key = xprvA35TEatf4ni4JQSNU7MGMAirXJuSjaCbtg31oZtwXGn1FVQs8qhP135XsTD3dnQ6Rwy396LHUvKXLAzV7ZVs84YLoauUxjt1HAa9xryFrsX
# name of wallet = Sponsor2

wallet = Wallet.create('azeiiéézeez', network = 'testnet')
print(wallet.get_key())
wallet.scan()
wallet.info()
t = wallet.send_to('xprvA35TEatf4ni4JQSNU7MGMAirXJuSjaCbtg31oZtwXGn1FVQs8qhP135XsTD3dnQ6Rwy396LHUvKXLAzV7ZVs84YLoauUxjt1HAa9xryFrsX', '0.1 BTC')

