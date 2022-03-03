from wireless import Wireless
import sys

def server_main():
    wireless = Wireless('server')
    wireless.send_message('Hello Client')
    print(wireless.recv_message())
    wireless.close()
    
def client_main():
    wireless = Wireless('client')
    print(wireless.recv_message())
    wireless.send_message('Hello Server')
    wireless.close()


if __name__ == '__main__':
    if sys.argv[1] == 'server':
        server_main()
    else:
        assert sys.argv[1] == 'client'
        client_main()