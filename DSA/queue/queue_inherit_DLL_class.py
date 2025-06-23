from doubly_linkedlist import DLL


class Deque(DLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0
        
    def is_empty(self):
        return super().is_empty()
    
    def insert_front(self, data):
        super().insert_at_start(data)
        self.item_count += 1
        
    def insert_rear(self,data):
        super().insert_at_last(data)
        self.item_count += 1
        
    def delete_front(self):
        if not self.is_empty():
            super().delete_first()
            self.item_count -= 1
        else:
            raise IndexError("Deque is empty!")
        
    def delete_rear(self):
       if not self.is_empty():
           super().delete_last()
           self.item_count -= 1
       else:
           raise IndexError("Deque is empty!")
       
    def get_front(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Deque is empty!")
        
    def get_rear(self):
        if not self.is_empty():
            temp = self.start
            while temp.next:
                temp = temp.next
            return temp.item
        else:
            raise IndexError("Deque is empty!")
            
    def size(self):
        return self.item_count
    

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

    # deq.delete_front()
    # deq.delete_rear()
    # deq.delete_rear()
    # deq.delete_front()
    # deq.delete_rear()

    print(f"Front=> {deq.get_front()}")
    print(f"Rear=> {deq.get_rear()}")
    print(f"Size=> {deq.size()}")


except IndexError as e:
    print(e)
