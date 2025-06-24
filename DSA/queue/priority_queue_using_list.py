class PriorityQueue:
    def __init__(self):
        self.li = []

    def is_empty(self):
        return len(self.li) == 0
    
    def push(self, priority_no, data):
        self.li.insert(priority_no, data)
    
    def pop(self,priority_no):
        if not self.is_empty():
            self.li.pop(priority_no)
        else:
            raise IndexError("Priority Queue is empty!")
        
    def size(self):
        return len(self.li)
        

pq = PriorityQueue()
print(pq.is_empty())

try:
    # print(f"Front=> {pq.get_front()}")
    # print(f"Rear=> {pq.get_rear()}")
    print(f"Size=> {pq.size()}")

    pq.push(1,20)
    pq.push(0, 10)
    pq.push(2,30)
    pq.push(3,40)
    pq.push(4,50)
    
    print(pq.li)
    print(f"Size=> {pq.size()}")
    
    pq.pop(4)

    print(pq.li)
    print(f"Size=> {pq.size()}")
    

except IndexError as e:
    print(e)

    
