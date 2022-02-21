import os
import requests
import time
os.system("title Discord - Send message to blocked user")
os.system("cls")
from colorama import Fore, init
init(convert=True)

class BlockBypass:
    def __init__(self, userId):
        self.channelId = "945163642494672936"
        self.userId = userId
        self.api = 'https://discord.com/api/v8/'
        self.headers = {
            'Authorization': "OTQ1MTYyNzEyNDE2MTQxMzQy.YhMKIA.uOQPgixKMBbSOEwQ5ud2l_wfGe4", #pun in token
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }

    def generateChannel(self):
        request = requests.post(f'{self.api}users/@me/channels', json={'recipients': [ self.userId ]}, headers=self.headers)

        if request.status_code == 200:
            print('Connected to API!\nConnected to channel...\n')
            self.channelId = request.json()['id']
            self.main()
        else:
            print('Couldn\'t create the channel!')
            print(request.status_code, request.json())
            exit(0)

    def sendMessage(self, message):
        request = requests.post(f'{self.api}channels/{self.channelId}/messages', json={'content': message}, headers=self.headers)

        if request.status_code == 200:
            print('Sent the message\n')
        else:
            print('Error')

        self.main()

    def main(self):
        content = input('-> ')

        self.sendMessage(content)

if __name__ == '__main__':
    print('\nDiscord devs momento, Ivano!\n\n')
    # Variables
    userId = input('ID to Message -> ')
    
    yesnt = BlockBypass(userId)
    yesnt.generateChannel()
    yesnt.main()