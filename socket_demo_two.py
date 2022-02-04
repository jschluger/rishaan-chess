# Client program
import socket
from time import sleep

HOST = ''                 # The remote host
PORT = 50008              # The same port as used by the server


with socket.socket() as s:
    # Join the socket "groupchat"
    s.connect((HOST, PORT))
    #sleep(5)

    while True:
        message = input('What would you like to say: ')
        print('Sending: ',message)
        
        s.send(message.encode())
        data = s.recv(1024)

        print('Received: ', data)