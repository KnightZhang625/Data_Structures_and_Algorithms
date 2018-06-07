# 顺序查找, 哨兵

class array_self(object):

    def __init__(self):
        self.array = []

    def add(self,item):
        self.array.append(item)

def sequentialSearch(list,target):

    i = len(list) - 1
    list.insert(0,target)

    while list[i] != target:
        i -= 1

    return i

if __name__ == '__main__':

    array = array_self()
    
    for i in range(10,0,-1):
        array.add(i)

    print(array.array)

    print(sequentialSearch(array.array,100))