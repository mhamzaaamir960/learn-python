class Queue:
    def __init__(self):
        self.items = []
        self.item_count = 0
        
    def is_emtpy(self):
        return len(self.items) == 0
    
    def enqueue(self, data):
        self.items.append(data)
        self.item_count += 1
   
    def dequeue(self):
        if not self.is_emtpy():
            self.items.pop(0)    
            self.item_count -= 1
    
    def get_front(self):
        if not self.is_emtpy():
            return self.items[0]
        else:
            raise IndexError("Queue is empty!")

    def get_rear(self):
        if not self.is_emtpy():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty!")
    
    def size(self):
        return self.item_count
    

queue = Queue()
print(queue.is_emtpy())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print(queue.is_emtpy())

    

print(queue.get_front())
print(queue.get_rear())
print(queue.size())

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

print()
print(queue.get_front())
print(queue.get_rear())
print(queue.size())
