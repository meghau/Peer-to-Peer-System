from socket import *
from transport import *
import thread

server_name = '127.0.0.1'
server_port = 7735
client_port = 5000
upload_port = 5678

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
#name = raw_input('Enter Host Name:')
name = '127.0.0.2'
client_socket.send(name + ' ' + str(client_port))
ack1 = client_socket.recv(1024)
print 'Server:'+ack1

peerSender = socket(AF_INET, SOCK_STREAM)
peerSender.bind((name, client_port))
peerSender.listen(5)

def process_peer():
    print ''

def connect_to_peer(name, upload_port):
    while True:
        peerReceiver, addr = peerSender.accept()
        thread.start_new_thread( process_peer, (peerReceiver, addr))
#try:
thread.start_new_thread(connect_to_peer, (name, upload_port))
#except:
#    print 'Unable to start Connect to other peers process'


while 1:
    #print '1. Connect to the Server \n2. Connect to a Peer'
    #connect_choice = raw_input('Enter your connection choice:')
    print "\n1. ADD an RFC to the server's index \n2. LOOKUP an RFC on the server's index \n3. LIST all RFCS"
    print "4. GET an RFC from a peer \n5. Exit from p2p System"
    choice = int(raw_input('Enter your choice:'))
    if choice == 1:
        print '\nEnter Details of the new RFC to be added'
        rfcno = raw_input('Enter RFC number:')
        #upload_port = raw_input('Enter upload port number:')
        rfc_title = raw_input('Enter RFC title:')
        request = create_rfc_request('ADD', rfcno, 'P2P-CI/1.0', name, upload_port, rfc_title)
        client_socket.send(request)
        ack2 = client_socket.recv(2048)
        print '\nMessage from Server:\n'+ack2+'\n'
    elif choice == 2:
        print 'Lookup'
    elif choice == 3:
        request = create_list_request(name, client_port)
        client_socket.send(request)
        response = client_socket.recv(4096)
        print '\nMessage from Server:\n'+response+'\n'
    elif choice == 5:
        print 'Exiting...'
        request = delete_request(name, client_port)
#    msg = peerReceiver.recv(1024)
#    print msg
client_socket.close()
