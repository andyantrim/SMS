# A.S.S Automated SMS System

This is an automated sms system that sends messages to multiple contacts. 

## Requirements
- Python 3
- pip3
- Account with Clockwork SMS

## Setting up
### API key, and contact list
The API key is copied into a text file found at /var/ass/api.key

The contacts are a csv that follows the format

name,number

Note that UK numbers that are normally +44 are actually just given as 44.

### Installing and running
from the home folder of program

`pip install -r requirements.txt`

To install the cli as a program called sms-cli run the install.sh script then do

`sms-cli -h`

To use the webserver simply run the python file src/web

From there server is avaliable locally on port 5000
