from clockwork import clockwork
from flask import Flask, render_template, request

import account
import sms

app = Flask(__name__)

api = clockwork.API(open("/var/ass/api.key", 'r').readline())


@app.route('/')
@app.route('/index')
def index():
    balance = account.check_balance(api)
    msgs = account.messages_left(api)

    return render_template('send.html', balance=str(balance), messages_left=str(msgs))

@app.route('/', methods=['POST'])
def send_form():
    msg = request.form['message']
    sender = request.form['number']
    sent = sms.send(api, sender, msg)

    return render_template('sent.html', message=msg, send_list=sent)

app.run(debug=True)
