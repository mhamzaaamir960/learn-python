from singly_linkedlist import SLL


class Stack(SLL):
    def __init__(self,start=None ):
        # super().__init__()
        self.start = start
        self.item_count = 0

    def is_empty(self):
        return super().is_empty()

    def push(self, data):
        super().insert_at_start(data)
        self.item_count += 1

    def pop(self):
        super().delete_first()
        self.item_count -= 1

    def peek(self):
        if not self.is_empty():
            return self.start.item

    def size(self):
        return self.item_count

    def insert_at_start(self, data):
        raise AttributeError("Stack has no 'insert_at_start' attribute!")

    def insert_at_last(self, data):
        raise AttributeError("Stack has no 'insert_at_last' attribute!")
    
    def insert_after(self, temp, data):
        raise AttributeError("Stack has no 'insert_after' attribute!")
 
    def print_values(self):
        raise AttributeError("Stack has no 'print_values' attribute!")
    
    def delete_first(self):
        raise AttributeError("Stack has no 'delete_first' attribute!")
    
    def delete_last(self):
        raise AttributeError("Stack has no 'delete_last' attribute!")
    
    def delete_item(self, data):
        raise AttributeError("Stack has no 'delete_item' attribute!")
    
    def search(self, data):
        raise AttributeError("Stack has no 'search' attribute!")
    

s = Stack()
print(s.is_empty())

for val in range(1,6):
    s.push(val*10)

print(s.peek())
s.pop()
print(s.peek())
