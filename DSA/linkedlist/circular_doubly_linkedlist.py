class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next


class CDLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        new_node = Node(item=data)
        if not self.is_empty():
            new_node.prev = self.start.prev
            new_node.next = self.start
            self.start.prev.next = new_node
            self.start.prev = new_node
            # self.start = new_node
        else:
            new_node.prev = new_node
            new_node.next = new_node
            # self.start = new_node

        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(item=data)
        if not self.is_empty():
            new_node.prev = self.start.prev
            new_node.next = self.start
            self.start.prev.next = new_node
            self.start.prev = new_node
        else:
            new_node.prev = new_node
            new_node.next = new_node
            self.start = new_node

    def search(self, data):
        temp = self.start
        if not self.is_empty():
            while temp:
                if temp.item == data:
                    return temp
                temp = temp.next
                if temp == self.start:
                    break

    def insert_after(self, temp, data):
        if temp:
            new_node = Node(temp, data, temp.next)
            temp.next.prev = new_node
            temp.next = new_node

    def print_values(self):
        if not self.is_empty():
            temp = self.start
            while temp:
                print(temp.item)
                temp = temp.next
                if temp == self.start:
                    break

    def delete_first(self):
        if not self.is_empty():
            if self.start == self.start.next:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next

    def delete_last(self):
        if not self.is_empty():
            if self.start == self.start.next:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev

    def delete_item(self, data):
        if not self.is_empty():
            temp = self.start
            while temp:
                if temp.item == data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    if temp == self.start:
                        self.start = self.start.next
                        if temp == temp.next:
                            self.start = None
                temp = temp.next
                if temp == self.start:
                    break
                
    def __iter__(self):
        return CDLLIterator(self.start)
    
class CDLLIterator:
    def __init__(self, start):
        self.start = start
        self.current = start
        self.flag = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if not self.current:
            raise StopIteration
        elif self.current == self.start and self.flag:
            raise StopIteration
        else:
            self.flag = True
        
        data = self.current.item
        self.current = self.current.next
        return data


l1 = CDLL()
l1.insert_at_last(30)
# l1.insert_at_start(10)
# l1.insert_after(l1.search(30),20)

# l1.print_values()
# print('\n\n')

# l1.delete_first()
# l1.delete_last()
# l1.delete_item(30)
# l1.print_values()

# print(l1.search(10).item)

for val in l1:
    print(val)
