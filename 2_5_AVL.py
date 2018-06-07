class TreeNode(object):

    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
        self.height = 1

class AVL_Tree(object):

    def __init__(self):
        pass

    def insert(self,root,key):

        if root == None:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left,key)
        elif key > root.val:
            root.right = self.insert(root.right,key)
        else:
            raise Exception('Element exits')

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        # LL
        if self.balance(root) > 1 and key < root.left.val:
            return self.Rr(root)

        # RR
        if self.balance(root) < -1 and key > root.right.val:
            return self.Lr(root)

        # LR
        if self.balance(root) > 1 and key > root.left.val:
            root.left = self.Lr(root.left)
            return self.Rr(root)

        # RL
        if self.balance(root) < -1 and key < root.right.val:
            root.right = self.Rr(root.right)
            return self.Lr(root)
        
        return root

    def Rr(self,z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    def Lr(self,z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    def getHeight(self,root):

        if root == None:
            return 0
        
        return root.height

    def balance(self,root):

        return self.getHeight(root.left) - self.getHeight(root.right)

    def display(self,root):

        if root == None:
            return
        else:
            self.display(root.left)
            print(root.val)
            self.display(root.right)

    def preOrder(self,root):
        
        if root == None:
            return
        else:
            print(root.val)
            self.test(root.left)
            self.test(root.right)

if __name__ == '__main__':

    myTree = AVL_Tree()

    root = None

    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)

    myTree.display(root)
    print(myTree.getHeight(root))




