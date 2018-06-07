class BinHeap(object):

    def __init__(self):

        self.heaplist = [0]
        self.currentSize = 0

    def percUp(self,i):

        while i // 2 != 0:
            if self.heaplist[i//2] > self.heaplist[i]:
                self.heaplist[i//2],self.heaplist[i] = self.heaplist[i],self.heaplist[i//2]
                i = i//2
            else:
                break

    def insert(self,val):

        self.heaplist.append(val)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percDown(self,i):

        while (i*2) <= self.currentSize:
            min_child_i = self.find_minChild(i)
            if self.heaplist[i] > self.heaplist[min_child_i]:
                self.heaplist[i],self.heaplist[min_child_i] = self.heaplist[min_child_i],self.heaplist[i]
                i = min_child_i
            else:
                break

    def find_minChild(self,i):

        if (i*2+1) > self.currentSize:
            return i*2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2 + 1

    def delete(self):

        min_num = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentSize]
        self.currentSize -= 1
        self.heaplist.pop()
        self.percDown(1)
        return min_num

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heaplist = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

if __name__ == '__main__':

    heap = BinHeap()
    # heap.insert(5)
    # heap.insert(10)
    # heap.insert(3)
    # heap.insert(2)

    # print(heap.heaplist)

    # heap.delete()
    # print(heap.heaplist)

    list_test = [9, 6, 5, 2, 3]
    heap.buildHeap(list_test)

    print(heap.heaplist)


