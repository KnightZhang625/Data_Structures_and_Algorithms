class Heap(object):

    def __init__(self):
        self.heap_list = [0]

    def display(self):

        return self.heap_list

    def add(self,node):
        
        self.heap_list.append(node)
        i = len(self.heap_list) - 1

        while i // 2 != 0:

            if self.heap_list[i].weight < self.heap_list[i//2].weight:
                self.heap_list[i],self.heap_list[i//2] = self.heap_list[i//2],self.heap_list[i]

            i = i // 2

    def delete(self):

        self.heap_list[1],self.heap_list[-1] = self.heap_list[-1],self.heap_list[1]
        node = self.heap_list.pop()
        i = 1

        while i * 2 < (len(self.heap_list) -1) :

            child_index = self.findMin(i)
            self.heap_list[i],self.heap_list[child_index] = self.heap_list[child_index],self.heap_list[i]
            i = child_index

        return node

    def findMin(self,i):

        if (i*2 + 1) > (len(self.heap_list) - 1):
            return i * 2
        else:
            if self.heap_list[i*2].weight < self.heap_list[i*2+1].weight:
                return i * 2
            else:
                return i * 2 + 1

class HuffmanTree(object):

    class Node(object):

        def __init__(self,weight=0,left=None,right=None):
            self.weight = weight
            self.left = left
            self.right = right
            self.code = ''

    def __init__(self):
        self.root = None
        self.heap = Heap()
        self.dic = {}

    def build(self,l):

        for i in l:
            self.heap.add(self.Node(i))

    def bulidHuffman(self):

        while len(self.heap.heap_list) > 2:

            node = self.Node()
            node.left = self.heap.delete()
            node.right = self.heap.delete()

            node.weight = node.left.weight + node.right.weight

            self.heap.add(node)

        self.root = self.heap.delete()

    def code(self,node):

        queue = [node]

        while len(queue) != 0:

            cur = queue.pop(0)
            if cur.left != None:
                queue.append(cur.left)
                cur.left.code = cur.code + '0'
            if cur.right != None:
                queue.append(cur.right)
                cur.right.code  = cur.code + '1'

        self.code_dic(self.root)

    def code_dic(self,root):

        if root.left == None and root.right == None:
            self.dic[root.weight] = root.code
        else:
            self.code_dic(root.left)
            self.code_dic(root.right)

if __name__ == '__main__':

    l = [5,2,1,10,3]

    h = HuffmanTree()

    h.build(l)

    test = h.heap.display()

    # for i in range(1,len(test)):
    #     print(test[i].weight)

    h.bulidHuffman()

    root = h.root

    queue = [root]

    while len(queue) != 0:

        cur = queue.pop(0)
        if cur.left != None:
            queue.append(cur.left)
        if cur.right != None:
            queue.append(cur.right)
        if cur.left == None and cur.right == None:
            print(cur.weight)

    h.code(root)

    print(h.dic)











