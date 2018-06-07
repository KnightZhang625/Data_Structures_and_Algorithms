class Union(object):

    class node(object):

        def __init__(self,data,parent):
            self.data = data
            self.parent = - parent

        def __str__(self):
            return str(self.data) + ' ' + str(self.parent) + '\n'

    def __init__(self):
        self.list_1 = []

    def add_union(self,single_union):

        length = len(single_union)
        father_index = len(self.list_1)

        father = self.node(single_union[0],length)

        self.list_1.append(father)

        for _,data in enumerate(single_union[1:]):
            self.list_1.append(self.node(data,-father_index))

    def find(self,data):

        length = len(self.list_1)

        i = 0

        while i < length:

            if self.list_1[i].data == data:
                
                while self.list_1[i].parent >= 0:
                    i = self.list_1[i].parent
                return i
            else:
                i += 1
        return False

    def merge(self,n1,n2):

        i1 = self.find(n1)
        i2 = self.find(n2)

        if abs(self.list_1[i1].parent) > abs(self.list_1[i2].parent):
            self.list_1[i1].parent += self.list_1[i2].parent
            self.list_1[i2].parent = - i1
        else:
            self.list_1[i2].parent += self.list_1[i1].parent
            self.list_1[i1].parent = -i2

if __name__ == '__main__':

    u1 = [1,3,5]
    u2 = [2,4,6]
    u3 = [7,8,9,10]

    union = Union()
    union.add_union(u1)
    union.add_union(u2)
    union.add_union(u3)

    for index,node in enumerate(union.list_1):
        print(str(index),'\t',node)

    union.merge(3,8)

    print()
    for index,node in enumerate(union.list_1):
        print(str(index),'\t',node)










