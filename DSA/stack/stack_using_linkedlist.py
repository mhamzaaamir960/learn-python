class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self, start=None):
        self.start = start
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0
    
    def push(self, data):
        new_node = Node(data, self.start)
        self.start = new_node
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.start = self.start.next
            self.item_count -= 1
        else:
            raise  Exception("Stack is empty!")
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise Exception("Stack is empty!")
        
    def size(self):
        return self.item_count
    

s = Stack()

for x in range(1,6):
    s.push(x*10)




# print(s.peek())
# s.pop()
# s.pop()
# print(s.peek())

while not s.is_empty():
    print(s.peek())
    s.pop()

print(s.peek())