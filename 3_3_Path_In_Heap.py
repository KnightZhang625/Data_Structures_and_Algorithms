class Heap(object):

    def __init__(self):

        self.list_heap = [0]
        self.currentSize = 0

    def insert(self,val):

        self.list_heap.append(val)
        self.currentSize += 1
        self._up(self.currentSize)

    def _up(self,i):

        while i//2 != 0:

            if self.list_heap[i] < self.list_heap[i//2]:
                self.list_heap[i],self.list_heap[i//2] = self.list_heap[i//2],self.list_heap[i]
                i = i//2
            else:
                break

    def delete(self):

        min_num = self.list_heap[1]
        self.list_heap[1] = self.list_heap[-1]
        self.currentSize -= 1
        self.list_heap.pop()
        self._down(1)
        return min_num

    def _down(self,i):

        while i*2 < self.currentSize:

            min_child = self._findChild(i)

            if self.list_heap[i] > self.list_heap[min_child]:
                self.list_heap[i],self.list_heap[min_child] = self.list_heap[min_child],self.list_heap[i]
                i *= 2
            else:
                break

    def _findChild(self,i):

        if i*2+1 > self.currentSize:
            return i * 2
        else:
            if self.list_heap[i*2] < self.list_heap[i*2+1]:
                return i*2
            else:
                return i*2+1

    def showPath(self,i):

        if i == 0:
            return
        else:
            print(self.list_heap[i])
            return self.showPath(i//2)

if __name__ == '__main__':

    heap = Heap()

    heap.insert(5)
    heap.insert(7)
    heap.insert(2)
    heap.insert(3)
    heap.insert(12)
    heap.insert(15)  
    heap.insert(50)
    heap.insert(30)
    heap.insert(80)
    heap.insert(25)
    heap.insert(21)
    heap.insert(32)
    heap.insert(1)

    print(heap.list_heap[1:])

    heap.delete()
    print(heap.list_heap[1:])

    heap.showPath(7)

