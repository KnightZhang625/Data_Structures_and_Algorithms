class Node(object):

    def __init__(self,val,left=None,right=None,height=1):

        self.val = val
        self.left = left
        self.right = right
        self.height = height

class AVL(object):

    def __init__(self):

        self.root = None

    def insert(self,val):

        self.root = self._insert(self.root,val)

    def _insert(self,root,val):

        if root == None:
            return Node(val)
        else:
            if val < root.val:
                root.left = self._insert(root.left,val)
            else:
                root.right = self._insert(root.right,val)

        root.height = max(self.getHeight(root.left),self.getHeight(root.right)) + 1

        # LL
        if self.balance(root) > 1 and val < root.left.val:
            return self.rightRotation(root)

        # RR
        if self.balance(root) < -1 and val > root.right.val:
            return self.leftRotation(root)

        # LR
        if self.balance(root) > 1 and val > root.left.val:
            root.left = self.leftRotation(root.left)
            return self.rightRotation(root)

        # RL
        if self.balance(root) < -1 and val < root.right.val:
            root.right = self.rightRotation(root.right)
            return self.leftRotation(root)

        return root

    def getHeight(self,root):

        if root == None:
            return 0 
        else:
            return root.height

    def balance(self,root):

        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotation(self,z):

        y = z.right
        T_temp = y.left

        y.left = z
        z.right = T_temp
       
        y.height = max(self.getHeight(y.left),self.getHeight(y.right)) + 1
        z.height = max(self.getHeight(z.left),self.getHeight(z.right)) + 1

        return y

    def rightRotation(self,z):

        y = z.left
        T_temp = y.right

        y.right = z
        z.left = T_temp

        y.height = max(self.getHeight(y.left),self.getHeight(y.right)) + 1
        z.height = max(self.getHeight(z.left),self.getHeight(z.right)) + 1

        return y

    def display(self,choice=1):

        if choice == 1:
            self._middleOrder(self.root)
        elif choice == 2:
            self._traverse(self.root)
        else:
            raise Exception('Invalid Choice')

        return ('finish')

    def _middleOrder(self,root):

        if root == None:
            return
        else:
            self._middleOrder(root.left)
            print(root.val)
            self._middleOrder(root.right)

    def _traverse(self,root):

        queue = [self.root]

        while len(queue) != 0:

            cur_node = queue.pop(0)

            if cur_node.left != None:
                queue.append(cur_node.left)
            if cur_node.right != None:
                queue.append(cur_node.right)

            print(cur_node.val)

    def find(self,val):

        return self._find(self.root,val)

    def _find(self,root,val):

        if root == None:
            return ('Not Exit')
        else:
            if val < root.val:
                return self._find(root.left,val)
            elif val > root.val:
                return self._find(root.right,val)
            else:
                return root

if __name__ == '__main__':

    avl = AVL()

    avl.insert(8)
    avl.insert(5)
    avl.insert(10)
    avl.insert(2)
    avl.insert(6)
    avl.insert(7)

    print(avl.display(2))












