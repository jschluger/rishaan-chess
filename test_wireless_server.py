from wireless import Wireless

def main():
    wireless = Wireless('server')


    wireless.send_message('Hello Client')
    print(wireless.recv_message())
    
    
    wireless.close()


if __name__ == '__main__':
    main()