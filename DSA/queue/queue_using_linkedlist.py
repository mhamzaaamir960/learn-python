class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Queue:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
        self.item_count = 0

    def is_empty(self):
        return self.front == None and self.rear == None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = self.rear.next
        self.item_count += 1

    def dequeue(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            self.item_count -= 1
        else:
            raise IndexError("Queue Underflow!")

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue Underflow!")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue Underflow!")

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
    
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    # q1.dequeue()
    # q1.dequeue()

    print()
    print(f"Front=>{q1.get_front()}")
    print(f"Rear=>{q1.get_rear()}")
except IndexError as e:
    print(e.args[0])



print(q1.size())
