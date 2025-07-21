# using recursion

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
        else:
            if self.root.item > data:
                self.root = self.insert()
        
