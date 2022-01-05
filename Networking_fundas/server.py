import socket
MAX_SIZE_BYTES = 65535
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# syntax for below follows
# socket.socket(family, type, proto, fileno)

# 1. Family: used to assign the type of assresses that a socket can communicate with. Only
# then can the address of that type be used with the socket
# There are three main options
# (a) AF_INET: This family used with IPV4 addresses
# (b) AF_INET6: This family used with IPV6 addresses 
# (c) AF_UNIX: This family is used for Unix Domain Sockets(UDS), an interprocess communication endpoint for
#               the same host.
# 2. Type: The type specifies the transport layer protocol
#    SOCK_DGRAM specifies that the application is to use User Datagram Protocol(UDP).
#    SOCK_STREAM specifies that the application is to use Transmission Control Protocol(TCP).
# More information can be found here https://docs.python.org/3/library/socket.html

#Binding the socket to a port and IP addrress
port = 3000
hostname = '127.0.0.1'
s.bind((hostname,port))
print('Listinig at {}'.format(s.getsockname()))

#running server infinetely otherwise it will only handle one message 
while True:
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES) #receive data from client
    message = data.decode('ascii') #decoding the message
    upperCaseMessage = message.upper() # converting it to a upper case
    print('The client at {} says {!r}'.format(clientAddress, message))
    data = upperCaseMessage.encode('ascii')
    s.sendto(data,clientAddress) # sending message back to the client

