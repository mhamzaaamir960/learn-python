from stack_using_linkedlist import Stack

class Node:
    def __init__(self, left=None, item=None, right=None):
        self.left = left
        self.item = item
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = root
    
    def inorder_traversal(self):
        s = Stack()
        temp = self.root
        while temp or s.size() > 0:
            while temp:
                s.push(temp)
                temp = temp.left
            temp = s.pop()
            print(temp.item, end=', ')
            temp = temp.right

    def insert(self, data):
        new_node = Node(item=data)
        temp = self.root
        if not self.root:
            self.root = new_node
        else:
            while temp.left or temp.right:
                if temp.item == data:
                    raise Exception("Item already exists")
                elif temp.item > data:
                    temp = temp.left
                elif temp.item < data:
                    temp = temp.right
            if temp.item > data:
                temp.left = new_node
            elif temp.item < data:
                temp.right = new_node
            elif temp.item == data:
                raise Exception("Item already exists")
            

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(20)
bst.insert(30)
# bst.insert(15)

# print(bst.root.item)
bst.inorder_traversal()
    
    