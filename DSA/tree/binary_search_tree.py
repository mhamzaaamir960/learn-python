from stack_using_linkedlist import Stack

class Node:
    def __init__(self, left=None, item=None, right=None):
        self.left = left
        self.item = item
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, data):
        new_node = Node(item=data)
        if not self.root:
            self.root = new_node
            return
        else:
            temp = self.root
            while temp:
                if temp.item == data:
                    raise Exception("Item already exists!")
                elif temp.item > data:
                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = new_node
                        return
                else:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = new_node 
                        return    
    def search(self, data):
        if self.root:
            temp = self.root
            if temp.item == data:
                return f"{temp.item} exits!"
            else:
                while temp:
                    if temp.item > data:
                        temp = temp.left
                    elif temp.item < data:
                        temp = temp.right

                    if temp and temp.item == data:
                        return f"{temp.item} exits!" 
        return None
                    
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
        
    def preorder_traversal(self):
        s = Stack()
        temp = self.root
        while temp or s.size() > 0:
            while temp:
                print(temp.item, end=', ')
                s.push(temp)
                temp = temp.left
            temp = s.pop()
            temp = temp.right
          

bst = BST()
bst.insert(50)
bst.insert(60)
bst.insert(40)
bst.insert(35)
bst.insert(45)
bst.insert(55)
bst.insert(65)
bst.insert(38)

print(bst.search(30))

bst.preorder_traversal()
    
    