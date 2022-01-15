blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    blockchain.append([last_transaction, transaction_amount])


add_value(2, [1])
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=3)
add_value(4, get_last_blockchain_value())

print(blockchain)
