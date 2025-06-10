class Stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self,data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is emtpy!")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty!")
    
    def size(self):
        if not self.is_empty():
            return len(self)
        else:
            raise IndexError("Stack is empty!")
    
    def insert(self,index,item):
        raise AttributeError("Stack has no 'insert' attribute!")
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
print(s1.peek())
print(s1.size())

s1.insert(1,5)
