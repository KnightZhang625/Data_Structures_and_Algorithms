class LinkedList(object):

    class _node(object):

        def __init__(self,data,next=None):

            self.data = data
            self.next = next

    def __init__(self):

        self.head = None

    def insert(self,data):

        if self.head == None:
            node = self._node(data)
            self.head = node
        else:
            self.test1(self.head,data)

    def test1(self,node,data):

        if node == None:
            return self._node(data)
        else:
            node.next = self.test1(node.next,data)
            return node

    def traverse(self):

        node = self.head

        while node != None:

            print(node.data)
            node = node.next

    def reverse_inner(self,node):

        if node.next == None:
            self.head = node
            return
        self.reverse_inner(node.next)
        temp = node.next
        temp.next = node
        node.next = None

def reverse(linklist):

    pre = None
    cur = linklist.head
    nex = cur.next

    while cur != None:

        cur.next = pre
        pre = cur
        cur = nex

        if nex:
            nex = nex.next

    linklist.head = pre
    return linklist


if __name__ == '__main__':

    l = LinkedList()
    l.insert(5)
    l.insert(4)
    l.insert(3)
    l.insert(2)
    l.insert(1)

    l.traverse()

    ll = reverse(l)
    ll.traverse()

    # l.reverse_inner(l.head)
    # l.traverse()







