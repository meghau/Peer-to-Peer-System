
from socket import *
from centralized_index import *
from transport import *
import thread

serverPort = 7735
peer_list = LinkedList()
rfc_list = LinkedList()


def process_client(connectionSocket, addr):
    clientInfo = connectionSocket.recv(1024)
    clientName, clientPort = clientInfo.split()
    peer_list.add(clientName, clientPort)
    connectionSocket.send('ack1')
    print 'Peer list:'
    peer_list.printList()
    print 'Rfc list:'
    rfc_list.printList()
    while 1:
        request = connectionSocket.recv(2048)
        if request != '':
            response = process_rfc_request(request, peer_list, rfc_list)
            connectionSocket.send(response)
            rfc_list.printList()
            #rfc_list.printList()
        elif request == 'FIN':
            connectionSocket.close()
            break

def MainThread():
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('127.0.0.1', serverPort))
    serverSocket.listen(5)

    print 'The server is ready to receive'
    while True:
        connectionSocket, addr = serverSocket.accept()
        #t = threading.Thread( target = self.__handlepeer, args = [ connectionSocket ] )
        thread.start_new_thread( process_client, (connectionSocket, addr))
        #t.start()

       # exit(0)
#connectionSocket.close()

if __name__ == "__main__":
    MainThread()