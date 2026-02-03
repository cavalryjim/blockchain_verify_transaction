# View an explanation of the code here: https://blog.agilephd.com/posts/blockchain_verify_tx/

from eth_account import Account

acct = Account.create()
private_key = acct.key
wallet_address = acct.address

tx = {
    "nonce": 0,
    "gasPrice": 1_000_000_000,
    "gas": 21000,
    "to": "0x000000000000000000000000000000000000d1a6",
    "value": 30000,
    "data": b"",
    "chainId": 1,
}

signed_tx = Account.sign_transaction(tx, private_key)

confirm_address = Account.recover_transaction(
    signed_tx.raw_transaction
)

print("wallet address:", wallet_address)
print("address recovered from the tx:", confirm_address)
print("valid:", wallet_address.lower() == confirm_address.lower())