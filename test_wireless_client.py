from wireless import Wireless

def main():
    wireless = Wireless('client')
    print(wireless.recv_message())
    wireless.send_message('Hello Server')
    wireless.close()
    
if __name__ == '__main__':
    main()