import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message", help="the message body to be sent via text")
parser.add_argument("sender", help="The name or number the message should be sent from")

args = parser.parse_args()
print("From:    " + str(args.sender))
print("Message: " + str(args.message))
