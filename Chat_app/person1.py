import socket
MAX_SIZE_BYTES = 65535
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 3000
hostname = '127.0.0.1'
s.bind((hostname,port))
print('Listinig at {}'.format(s.getsockname()))

#running server infinetely otherwise it will only handle one message 
while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES) #receive data from client
    message = data.decode('ascii') #decoding the message
    print('The client at {} says {!r}'.format(clientAddress, message))
    my_message = input('Type your message here: ') # message/text you want to send    
    data = my_message.encode('ascii')
    s.sendto(data,clientAddress) # sending message back to the client