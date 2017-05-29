from clockwork import clockwork
import time

contacts = open("../data/contacts.csv", 'r').readlines()

def send(api, from_name, payload, test=True):
    resp_list = []
    print("Sent from: " + from_name)
    if test:
        print("TEST MODE")
    for contact in contacts:
        contents = contact.split(",")
        name = contents[0]
        number = contents[1]

        msg = clockwork.SMS(
                from_name=from_name,
                to=number,
                message="Hi, " + name + " " + payload
                )

        if not test:
            rep = api.send(msg)
        else:
            print(msg.to.strip() + ": " + msg.message)
        resp_list.append(str(msg.to.strip() + ": " + msg.message))
    return resp_list

if __name__ == "__main__":
    send("Andy&Amy", "This is a test for some stuff")

