class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def insert_front(self, data):
        self.items.insert(0, data)

    def insert_rear(self, data):
        self.items.append(data)

    def delete_front(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Deque is empty!")
        
    def delete_rear(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError("Deque is emtpy!")
        
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else: 
            raise IndexError("Deque is empty!")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque is empty!")
        
    def size(self):
        return len(self.items)
    


deq = Deque()
print(deq.is_empty())

try:
    # print(f"Front=> {deq.get_front()}")
    # print(f"Rear=> {deq.get_rear()}")
    # print(f"Size=> {deq.size()}")

    deq.insert_rear(20)
    deq.insert_rear(30)
    deq.insert_front(10)
    deq.insert_rear(40)
    deq.insert_front(5)

    deq.delete_front()
    deq.delete_rear()
    deq.delete_rear()
    deq.delete_front()
    # deq.delete_rear()

    print(f"Front=> {deq.get_front()}")
    print(f"Rear=> {deq.get_rear()}")
    print(f"Size=> {deq.size()}")



except IndexError as e:
    print(e)