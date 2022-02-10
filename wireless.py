import socket


class Wireless():
    # which_type should be 'server' or 'client' 
    def __init__(self, which_type):
        if which_type == 'server':
            HOST = ''                 # Symbolic name meaning all available interfaces
            PORT = 50008              # Arbitrary non-privileged port

            with socket.socket() as s:
                s.bind((HOST, PORT))

                # Listen for one connection
                s.listen()
                
                # Wait until someone else joins this (HOST,PORT) specified socket
                self.conn, addr = s.accept()
                print('Connected by', addr)

        else:
            assert which_type == 'client'
            HOST = socket.gethostbyname(socket.gethostname())  # The remote host
            PORT = 50008              # The same port as used by the server

            with socket.socket() as s:
                # Join the socket "groupchat"
                s.connect((HOST, PORT))
                #sleep(5)
                self.conn = s

            

    def send_message(self, message):
        self.conn.send(message.encode())

    def recv_message(self):
        data = self.conn.recv(1024)
        return data


    def server_talk(self):
        while True:
            # Recieve data on the connection
            data = self.conn.recv(1024)
            print('Recieved: ',data)
            # sleep(5)

            # Reply to the other program
            reply = input('What would you like to say: ')
            print('Sending: ',reply)
            self.conn.send(reply.encode())


    def client_talk(self):
        while True:
            message = input('What would you like to say: ')
            print('Sending: ',message)
            
            self.conn.send(message.encode())
            data = self.conn.recv(1024)

            print('Received: ', data)


