
class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def push(self, data):
        if self.is_empty():
            self.top = 0
        else:
            self.top += 1
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            if len(self.stack) == 1:
                self.top = -1
            else:
                self.top -= 1
            self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        else:
            return "Stack is empty!"

    def size(self):
        if self.is_empty():
            return "Stack is empty!"
        else:
            self.top += 1
            return self.top
        
s1 = Stack()
print(s1.is_empty())
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)

# s1.pop()

while not s1.is_empty():
    print(s1.peek())
    s1.pop()


# print(s1.peek())
