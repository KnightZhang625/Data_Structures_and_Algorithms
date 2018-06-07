class BinaryTree(object):

    class Node(object):

        def __init__(self,data=None,left=None,right=None):
            self._data = data
            self._left = left
            self._right = right

    def __init__(self,data=None):
        node = self.Node(data)
        self._root = node

    def isEmpty(self):
        return self._root == None

    def add(self,data):
        
        node = self.Node(data)
        queue = []

        if self._root == None:
            self._root = node
        else:
            queue.append(self._root)

            while len(queue) != 0:
                cur = queue[0]
                if cur._left == None:
                    cur._left = node
                    return True
                elif cur._right == None:
                    cur._right = node
                    return True
                else:
                    queue.append(cur._left)
                    queue.append(cur._right)
                queue.pop(0)

    # 层序遍历
    def display(self):

        queue = []

        if self._root == None:
            return None
        else:
            queue.append(self._root)

            while len(queue) != 0:
                cur = queue.pop(0)
                if cur._left != None:
                    queue.append(cur._left)
                if cur._right != None:
                    queue.append(cur._right)
                print(cur._data)

    # 先序遍历
    def preOrderTravel(self,node):
        
        if node != None:
            print(node._data)
            self.preOrderTravel(node._left)
            self.preOrderTravel(node._right)
        else:
            return

    def display2(self):
        if self._root == None:
            return False
        else:
            self.preOrderTravel(self._root)

    def preStack(self):

        if self._root == None:
            return False
        else:
            stack = [] 
            node = self._root

            while (node != None or len(stack) != 0):

                while node:
                    print(node._data)
                    stack.append(node)
                    node = node._left
                if (len(stack) != 0):
                    node = stack.pop()
                    node = node._right

    # 中序遍历
    def middleOrderTravel(self,node):

        if node != None:
            self.middleOrderTravel(node._left)
            print(node._data)
            self.middleOrderTravel(node._right)
        else:
            return

    def display3(self):
        if self._root == None:
            return False
        else:
            self.middleOrderTravel(self._root)

    def middleStack(self):

        if self._root == None:
            return False
        else:
            stack = []
            node = self._root
            while(len(stack)!=0 or node != None):
                while node:
                    stack.append(node)
                    node = node._left
                if(len(stack)!=0):
                    node = stack.pop()
                    print(node._data)
                    node = node._right

    # 后序遍历
    def backOrderTravel(self,node):

        if node != None:
            self.backOrderTravel(node._left)
            self.backOrderTravel(node._right)
            print(node._data)
        else:
            return False

    def display4(self):
        if self._root == None:
            return False
        else:
            self.backOrderTravel(self._root)

if __name__ == '__main__':

    tree = BinaryTree('a')
    tree.add('b')
    tree.add('c')
    tree.add('d')
    tree.add('e')
    tree.add('f')
    tree.display()
    print()
    tree.display2()
    tree.preStack()
    print()
    tree.display3()
    tree.middleStack()
    print()
    tree.display4()
    tree.backStack()














