from django.apps import AppConfig
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0xEDcF7ffD914DA6e50F2282f1a998Bbd021030C3b"
account_2 = "0xed2a4eB8546679fE150768b0258e6223a85484F1"

private_key = "0xf8d6f26d0954924bcddd00b3816f3c65b120d1f51fd4e5f52d4a12581a25c8d3"

nonce = web3.eth.get_transaction_count(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.to_wei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei'),
}

signed_tx = web3.eth.account.sign_transaction(tx, private_key)

tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

print(web3.to_hex(tx_hash))
print("Transaction succesfull!")


class AppConfig(AppConfig):
    name = 'app'
