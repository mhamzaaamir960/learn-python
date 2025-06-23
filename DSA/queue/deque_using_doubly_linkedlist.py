class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.front == None

    def insert_front(self, data):
        new_node = Node(item=data, next=self.front)
        if self.is_empty():
            self.rear = new_node
        else:
            # new_node.next = self.front
            self.front.prev = new_node

        self.front = new_node
        self.item_count += 1

    def insert_rear(self, data):
        new_node = Node(self.rear, data)
        if self.is_empty():
            self.front = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
        self.rear = new_node
        self.item_count += 1

    def delete_front(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = None
            self.item_count -= 1
        else:
            raise IndexError("Deque is empty!")

    def delete_rear(self):
        if not self.is_empty():
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
            self.item_count -= 1

        else:
            raise IndexError("Deque is emtpy!")

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Deque is empty!")

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
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

    deq.delete_front()
    deq.delete_rear()
    deq.delete_rear()
    # deq.delete_front()
    # deq.delete_rear()

    print(f"Front=> {deq.get_front()}")
    print(f"Rear=> {deq.get_rear()}")
    print(f"Size=> {deq.size()}")


except IndexError as e:
    print(e)
