from centralized_index import *


def create_rfc_request(method, rfcno, version, host, port, title):
    request = method.upper() + ' RFC ' + str(rfcno) + ' ' + version + '\n'
    request += 'Host: ' + host + '\n' + 'Port: ' + str(port) + '\n'
    if method == 'ADD' or method == 'LOOKUP':
        request += 'Title: ' + title
    return request

def create_list_request(hostname, client_port):
    request = 'LIST ALL P2P-CI/1.0\nHost: '+ hostname +'\nPort: '+ str(client_port)
    return request

def process_rfc_request(request, peer_list, rfc_list):
    parsed_request = request.split('\n')
    method = parsed_request[0].split()[0]
    response = ''
    host = parsed_request[1].split()[1]
    port = parsed_request[2].split()[1]

    if method == 'ADD':
        print 'ADD'
        rfcno, version = parsed_request[0].split()[2:]
        title = parsed_request[3].split(':')[1]
        rfc_list.add(rfcno, title, host)
        response += version + ' 200 OK\nRFC ' + rfcno + ' ' + title + ' ' + host + ' ' + port

    elif method == 'LOOKUP':
        print 'LOOKUP'
        rfcno, version = parsed_request[0].split()[2:]
        title = parsed_request[3].split(':')[1]
        flag = 0
        rfc_iter = rfc_list.root
        while rfc_iter:
            if rfc_iter.get_rfcno() == rfcno:
                flag = 1
                h = rfc_iter.get_hostname()
                p = find_port(h, peer_list)
                response += '\n' + h + ' ' + p
            rfc_iter = rfc_iter.get_next()
        if flag == 1:
            response = version + ' 200 OK ' + response
        else:
            response = '404 NOT FOUND'

    elif method == 'LIST':
        print 'LIST REQUEST'
        version = parsed_request[0].split()[2]
        rfc_iter = rfc_list.root
        #print rfc_list.get_size()
        while rfc_iter:
            rno = rfc_iter.get_rfcno()
            t = rfc_iter.get_rfcname()
            h = rfc_iter.get_hostname()
            p = find_port(h, peer_list)
            response += '\nRFC' + rno + ' ' + t + ' ' + h + ' '
            rfc_iter = rfc_iter.get_next()
        if response == '':
            response = '404 NOT FOUND'
        else:
            response = version + ' 200 OK ' + response
    return response











