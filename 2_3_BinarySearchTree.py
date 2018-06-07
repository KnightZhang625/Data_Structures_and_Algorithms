class BinarySearchTree(object):

    class Node(object):

        def __init__(self,data=None,left=None,right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self,data=None):

        if data == None:
            self.root = None
        else:
            node = self.Node(data)
            self.root = node

    def find(self,data):

        return self._fun1(data,self.root)

    def _fun1(self,data,node):

        if node == None:
            return False
        else:
            if data < node.data:
                return self._fun1(data,node.left)
            elif data > node.data:
                return self._fun1(data,node.right)
            else:
                return True

    def add(self,data):
        
        self.root = self._fun2(data,self.root)

    def _fun2(self,data,node):
        
        if self.find(data):
            return ('the element exits')
        else:
            if self.root == None:
                self.root = self.Node(data)
            else:
                if node == None:
                    node = self.Node(data)
                elif data < node.data:
                    node.left = self._fun2(data,node.left)
                else:
                    node.right = self._fun2(data,node.right)
                return node

    def display(self):
        
        if self.root == None:
            return False
        else:
            self._fun3(self.root)

    def _fun3(self,node):

        if node == None:
            return
        else:
            self._fun3(node.left)
            print(node.data)
            self._fun3(node.right)

    def findMin(self):
        
        if self.root == None:
            return False
        else:
            return self._fun4(self.root)

    def _fun4(self,node):

        if node.left == None:
            return node.data
        else:
            return self._fun4(node.left)

    def findMax(self):

        if self.root == None:
            return False
        else:
            node = self.root.right
            while(node.right):
                node = node.right
            return node.data

    def delete(self,data):

        if not self.find(data):
            return False
        else:
            self._fun5(data,self.root)

    def _fun5(self,data,node):

        if data < node.data:
            node.left = self._fun5(data,node.left)
        elif data > node.data:
            node.right = self._fun5(data,node.right)
        else:
            if (node.left and node.right):

                temp = self._fun4(node.right)
                node.data = temp
                node.right = self._fun5(temp,node.right)
            else:
                if not node.left:
                    node = node.right
                elif not node.right:
                    node = node.left
        return node

if __name__ == '__main__':

    tree = BinarySearchTree(3)
    tree.add(5)
    tree.add(6)
    tree.add(1)
    tree.add(10)
    tree.add(7)

    tree.display()

    tree.delete(7)
    tree.display()
















