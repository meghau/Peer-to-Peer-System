class PeerNode(object):
    def __init__(self, h, p, n = None):
        self.hostname = h
        self.port = p
        self.next_node = n

    def get_hostname(self):
        return self.hostname

    def set_hostname(self,h):
        self.hostname = h

    def get_port(self):
        return self.port

    def set_port(self, p):
        self.port = p

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def info(self):
        return self.get_hostname()+' '+str(self.get_port())

class RFCNode(object):
    def __init__(self, rno, rname, h, n=None):
        self.rfcno = rno
        self.rfcname = rname
        self.hostname = h
        self.next_node = n

    def get_rfcno(self):
        return self.rfcno

    def set_rfcno(self,rno):
        self.rfcno = rno

    def get_rfcname(self):
        return self.rfcname

    def set_rfcname(self,rname):
        self.rfcname = rname

    def get_hostname(self):
        return self.hostname

    def set_hostname(self,h):
        self.hostname = h

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def info(self):
        return str(self.get_rfcno())+' '+self.get_rfcname()+' '+self.get_hostname()

class LinkedList(object):
    def __init__(self, r= None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, *arg):
        #new_node=''
        if len(arg) == 2 :
            new_node = PeerNode(arg[0], arg[1], self.root)
            print 'peer node created'
        elif len(arg) == 3:
            new_node = RFCNode(arg[0], arg[1], arg[2], self.root)
            print 'rfc node created'
        self.root = new_node
        self.size += 1

    def remove(self, h):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_hostname() == h:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def printList(self):
        this_node = self.root
        while this_node:
            print this_node.info()
            this_node = this_node.get_next()


def find_port(h, peer_list):
    this_node = peer_list.root
    while this_node:
        if this_node.get_hostname() == h:
            return this_node.get_port()
        this_node = this_node.get_next()
    return None

#l = LinkedList()
#l.add('megha',1234)
#l.add('megha1',31234)
#l.add('megha2',41234)
#l.add('megha3',51234)
#print l.remove('megha3')
#l.printList()
