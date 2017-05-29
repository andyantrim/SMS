from clockwork import clockwork

def check_balance(api):
    balance = api.get_balance()
    return balance['balance']

def messages_left(api):
    balance = api.get_balance()
    cash = float(balance['balance'])

    # How many contacts are on the list
    msg_needed = 0
    for line in open("../data/contacts.csv", 'r').readlines():
        msg_needed = msg_needed + 1

    # Balance / .05 gives amount of messages we can send
    capacity = cash/.05

    # Group messages left is capacity/number of contacts
    msg_left = int(capacity/msg_needed)

    return msg_left


