class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        new_node = Node(data, next=self.start)
        if self.start:
            self.start.prev = new_node
        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.start = new_node
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(data, prev=temp, next=temp.next)
            if temp.next is not None:
                temp.next.prev = new_node
            temp.next = new_node

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp is None:
            return None

    def delete_first(self):
        if self.start:
            temp = self.start
            self.start = temp.next
            if self.start:
                self.start.prev = None
            return temp.item

    def delete_last(self):
        temp = self.start
        if not temp:
            pass
        elif not temp.next:
            self.start = None
        else:
            while temp.next.next:
                temp = temp.next
            temp.next.prev = None
            temp.next = None
        return self.start

    def delete_item(self, data):
        if not self.start:
            pass
        elif not self.start.next and self.start.item == data:
            self.start = None
        else:
            temp = self.start
            while temp:
                if temp.item == data:
                    if temp.prev:
                        temp.prev.next = temp.next
                        if temp.next:
                            temp.next.prev = temp.prev
                    else:
                        self.start = temp.next
                        self.start.prev = None
                    break
                temp = temp.next

    def print_values(self):
        if self.start:
            temp = self.start
            while temp:
                print(temp.item)
                temp = temp.next

    def __iter__(self):
        return DLLIterator(self.start)


class DLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


node = DLL()

node.insert_at_last(20)
node.insert_at_start(10)
node.insert_at_last(40)
node.insert_after(node.search(20), 30)
node.insert_at_last(50)

node.delete_item(30)


for val in node:
    print(val, end=" ")

print()
