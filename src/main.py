from clockwork import clockwork
import argparse

import account
import sms

def main():
    api = clockwork.API(open("/var/ass/api.key", 'r').readline())
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="the message body to be sent via text")
    parser.add_argument("sender", help="The name or number the message should be sent from")

    args = parser.parse_args()

    #Check the balance and check how many more messages we can send to all contacts
    balance = account.check_balance(api)
    print("$" + balance)
    msgs = account.messages_left(api)
    print("msgs remaining before top up " + str(msgs))

    sms.send(api, args.sender, args.message)

if __name__ == "__main__":
    main()
