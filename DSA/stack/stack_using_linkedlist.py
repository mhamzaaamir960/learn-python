class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self, start=None):
        self.__start = start
        self.__item_count = 0

    def is_empty(self):
        return self.__start == None
    
    def push(self, data):
        new_node = Node(data, self.__start)
        self.__start = new_node
        self.__item_count += 1

    def pop(self):
        if not self.is_empty():
            data = self.__start.item
            self.__start = self.__start.next
            self.__item_count -= 1
            return data
        else:
            raise  Exception("Stack is empty!")
        
    def peek(self):
        if not self.is_empty():
            return self.__start.item
        else:
            raise Exception("Stack is empty!")
        
    def size(self):
        return self.__item_count
    

s = Stack()

for x in range(1,6):
    s.push(x*10)




# print(s.peek())
# s.pop()
# s.pop()
# print(s.peek())
print(f'Items count: {s.size()}')

while not s.is_empty():
    print(s.peek())
    s.pop()

# print(s.peek())

print(f'Items count: {s.size()}')
