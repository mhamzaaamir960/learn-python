class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next


class PriorityQueue:
    def __init__(self, start=None):
        self.start = start 
        self.item_count = 0
    
    def is_empty(self):
        return self.start == None
    
    def push(self, data, priority):
        new_node = Node(data, priority)
        if self.is_empty():
            self.start = new_node
        else:
            temp = self.start
            if temp.priority >= priority:
                new_node.next = temp
                self.start = new_node
            else:
                while temp.next and temp.next.priority < priority:
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
        self.item_count += 1
    
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise Exception("Priority Queue is empty!")
        
    def size(self):
        return self.item_count
    
p = PriorityQueue()
print(p.is_empty())
print(p.size())


p.push("Hamza", 4)
p.push("Omer",2)
p.push("Ahmed", 5)
p.push("Hassan",1)
p.push("Fazeel",10)
p.push("Ibrahim",7)
print(p.size())



while not p.is_empty():
    print(p.pop())

print(p.size())
