from socket import *
from transport import *

serverName = 'localhost'
serverPort = 7735
clientPort = 5001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
#name = raw_input('Enter Host Name:')
name = gethostbyname(gethostname())
clientSocket.send(name+' '+str(clientPort))
ack1 = clientSocket.recv(1024)
print 'Server:'+ack1
#request = create_rfc_request('ADD', 123, 'P2P-CI/1.0', 'thishost.csc.ncsu.edu', 5678, 'A Proferred Official ICP')
request = 'LIST ALL P2P-CI/1.0\nHost: thishost.csc.ncsu.edu\nPort: 5678'
clientSocket.send(request)
ack2 = clientSocket.recv(2048)
print 'Server:'+ack2
#clientSocket.listen(5)
#while True:
#    peerSocket, addr = clientSocket.accept()
#peerSocket = socket(AF_INET, SOCK_STREAM)
#peerSocket.connect((serverName, 5000))
#peerSocket.send('connecting to client 1...')
#clientSocket.close()
