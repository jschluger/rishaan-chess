# Server program
import socket
from time import sleep

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port

# s = socket.socket()
with socket.socket() as s:
    s.bind((HOST, PORT))

    # Listen for one connection
    s.listen()
    print('Listening for a connection...')

    # Wait until someone else joins this (HOST,PORT) specified socket
    conn, addr = s.accept()
    print('Connected by', addr)

    while True:
        # Recieve data on the connection
        data = conn.recv(1024)
        print('Recieved: ',data)
        # sleep(5)

        # Reply to the other program
        reply = input('What would you like to say: ')
        print('Sending: ',reply)
        conn.send(reply.encode())

# s is gone

