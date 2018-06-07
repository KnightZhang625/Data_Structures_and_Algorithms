class Union(object):

    class Node(object):

        def __init__(self,val,parent):
            self.val = val
            self.parent = parent

        def __str__(self):
            return str(self.val) + ' ' + str(self.parent)

    def __init__(self):
        self.list1 = []

    def insert(self,u):
        
        length = len(u)
        father = self.Node(u[0],-length)
        self.list1.append(father)
        father_index = len(self.list1) - 1

        for i in u[1:]:
            node = self.Node(i,father_index)
            self.list1.append(node)

    def find(self,i):
        
        if self.list1[i].parent < 0:
            return i
        else:
            return self.find(self.list1[i].parent)

    def merge(self,n1,n2):
        
        f1 = self.find(n1)
        f2 = self.find(n2)

        if abs(self.list1[f1].parent) > abs(self.list1[f2].parent):
            self.list1[f1].parent += self.list1[f2].parent
            self.list1[f2].parent = f1
        else:
            self.list1[f2].parent += self.list1[f1].parent
            self.list1[f1].parent = f2

    def connect(self):

        count = 0

        for i in self.list1:
            if i.parent < 0:
                count += 1
        if count == 1:
            return True
        else:
            return False

if __name__ == '__main__':

    u1 = [2,5,7]
    u2 = [1,3,6]
    u3 = [10,12,15,18,20]

    union = Union()
    union.insert(u1)
    union.insert(u2)
    union.insert(u3)

    for i in union.list1:
        print(i,'\t')

    union.merge(3,10)

    print()
    for i in union.list1:
        print(i,'\t')

    print(union.connect())













