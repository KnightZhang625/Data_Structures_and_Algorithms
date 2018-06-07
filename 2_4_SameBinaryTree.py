class BinaryTree(object):

    class Node(object):

        def __init__(self,data=None,left=None,right=None,flag=False):

            self._data = data
            self._left = left
            self._right = right
            self._flag = flag

    def __init__(self):

        self.root = None

    def find(self,data):
        if self.root == None:
            raise Exception('Empty tree')
        else:
            return self.find_inner(self.root,data)

    def find_inner(self,root,data):

        if root == None:
            return False
        else:
            if data < root._data:
                return self.find_inner(root._left,data)
            elif data > root._data:
                return self.find_inner(root._right,data)
            else:
                return True


    # 增加节点
    def add(self,data):

        if self.root == None:
            node = self.Node(data)
            self.root = node
        else:
            self.add_inner(self.root,data)

    def add_inner(self,root,data):

        if root == None:
            root = self.Node(data)
        else:
            if data < root._data:
                root._left = self.add_inner(root._left,data)
            elif data > root._data:
                root._right = self.add_inner(root._right,data)
            else:
                raise Exception('Element exits')

        return root

    # 中序遍历
    def display(self):

        self.display_inner(self.root)

    def display_inner(self,root):

        if root == None:
            return
        else:
            self.display_inner(root._left)
            print(root._data)
            self.display_inner(root._right)

    # 树的高度
    def height(self,node):
        if node == None:
            return 0
        else:
            l_height = self.height(node._left)
            r_height = self.height(node._right)
            return max(l_height,r_height) + 1

    def balance(self,root):
        if root == None:
            return True
        else:
            if abs(self.height(root._left) - self.height(root._right)) > 1:
                return False
            else:
                return self.balance(root._left) and self.balance(root._right)


# 输入两棵树判断
def equal(t1,t2,temp):

    if t1 == None and t2 == None:
        return temp
    elif t1 == None or t2 == None:
        return False
    elif t1._data != t2._data:
        return False
    else:
        temp = equal(t1._left,t2._left,temp)
        temp = equal(t1._right,t2._right,temp)
    return temp

if __name__ == '__main__':

    b = BinaryTree()
    b.add(5)
    b.add(3)
    b.add(7)
    b.add(10)
    b.add(1)
    b.add(2)
    b.display()

    c = BinaryTree()
    c.add(5)
    c.add(3)
    c.add(7)

    print(b.height(b.root))
    print(c.balance(c.root))










