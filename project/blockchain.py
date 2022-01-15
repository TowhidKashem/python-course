blockchain = []


def get_last_blockchain_value():
    if len(blockchain) > 0:
        return blockchain[-1]
    return None


def add_value(transaction_amount, last_transaction):
    if last_transaction == None:
        last_transaction = [1.0]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return float(input("Your transaction amount: "))


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('block:', block)


while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: for quit')

    user_choice = get_user_choice()
    if user_choice == '1':
        transaction_amount = get_transaction_value()
        add_value(transaction_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Invalid input, pick a value from the list')


# print(blockchain)
