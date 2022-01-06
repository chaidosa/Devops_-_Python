import socket
MAX_SIZE_BYTES = 65535
port = 3000
hostname = '127.0.0.2'
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((hostname,port))
print('Listinig at {}'.format(s.getsockname()))

while True:
    message = input('Input the text that you want to send: ')
    data = message.encode('ascii')
    s.sendto(data,('127.0.0.1',port))
    print('The OS assigned the address {} to me'.format(s.getsockname()))
    data, address = s.recvfrom(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    print('The server {} replied with {!r}'.format(address, text))