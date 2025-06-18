from singly_linkedlist import SLL


class Queue:
    def __init__(self):
        self.li = SLL()
        self.item_count = 0
    
    
    def is_empty(self):
        return self.li.is_empty()
    
    def enqueue(self, data):
        self.li.insert_at_last(data)
        self.item_count += 1
        
    def dequeue(self):
        if not self.is_empty():
            self.li.delete_first()
            self.item_count -= 1
        else:
            raise IndexError("Queue is Empty!")
    
    def get_front(self):
        if not self.is_empty():
            return self.li.start.item
        else:
            raise IndexError("Queue is Empty!")
    
    def get_rear(self):
        if not self.is_empty():
            temp = self.li.start
            while temp.next:
                temp = temp.next
            print(temp.item)
        else:
            raise IndexError("Queue is Empty!")
        
    def size(self):
        return self.item_count
    
    
q1 = Queue()
# print(q1.size())

# try:
#     print(q1.get_front())
# except IndexError as e:
#     print(e)


q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)

try:
    print(f"Front=>{q1.get_front()}")
    print(f"Rear=>{q1.get_rear()}")
    print(q1.size())

    
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    # q1.dequeue()

    print()
    print(f"Front=>{q1.get_front()}")
    print(f"Rear=>{q1.get_rear()}")
except IndexError as e:
    print(e.args[0])



print(q1.size())



        
        
        
