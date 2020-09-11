# Author : Orion F
# This app allows you to extract data of a user profile using fbchat module. The goal is to allow the program to send a message to user or group. Enjoy!

# pip install fbchat

# import modules
from fbchat import Client
from fbchat.models import Message

username = "(YOUR FB EMAIL)"
password = "************"


# login fb
client = Client(username, password)


print('Own id: {}'.format(client.uid))


users = client.searchForUsers('him.orion.7')
user = users[0]
print("User's ID: {}".format(user.uid))
print("User's name: {}".format(user.name))
print("User's profile picture URL: {}".format(user.photo))
print("User's main URL: {}".format(user.url))

# logout from fb
client.logout()
