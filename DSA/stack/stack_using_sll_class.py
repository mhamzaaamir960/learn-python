
from singly_linkedlist import SLL


class Stack:
    def __init__(self):
        self.myList = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.myList.is_empty()
    
    def push(self,data):
        self.myList.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            deleted_item = self.myList.start.item
            self.myList.delete_first()
            self.item_count -= 1
            return deleted_item
        else:
            raise Exception("Stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.myList.start.item
        else:
            raise Exception("Stack is empty!")

    def size(self):
        return self.item_count
    

s = Stack()
print(s.is_empty())
for value in range(1,6):
    s.push(value*10)

print(s.peek())
print(s.pop())
print(s.peek())

