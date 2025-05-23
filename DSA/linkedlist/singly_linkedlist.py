class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        new_node = Node(data, self.start)
        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if not self.is_empty():
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = new_node
        else:
            self.start = new_node

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            new_node = Node(data, temp.next)
            temp.next = new_node

    def delete_first(self):
        temp = self.start
        if temp is not None:
            self.start = temp.next
            return temp.item

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = temp.next.next

    def delete_item(self, data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                value = self.start.item
                self.start.item = None
                return value
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        value = temp.next.item
                        temp.next = temp.next.next
                        return value
                    temp = temp.next

    def print_values(self):
        temp = self.start
        while temp is not None:
            print(temp.item)
            temp = temp.next

    def __iter__(self):
        return SLLIterator(self.start)


class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


li = SLL()

# print(li.is_empty())
li.insert_at_start(30)
li.insert_at_start(20)
li.insert_at_last(40)
li.insert_at_start(10)
li.insert_at_last(50)

li.insert_after(li.search(20), 25)


li.print_values()

# print(li.search(40))

# print(li.is_empty())

# for value in li:
#     print(f"value: {value}")


# print(li.delete_first())
# print(li.delete_first())
# print(li.delete_first())

# li.delete_last()
# li.delete_last()
# li.delete_last()
# li.delete_last()

# print(f"deleted item: {li.delete_item(30)}")
# print(f"deleted item: {li.delete_item(25)}")
# print(f"deleted item: {li.delete_item(40)}")
# print(f"deleted item: {li.delete_item(50)}")
# print(f"deleted item: {li.delete_item(20)}")
print(f"deleted item: {li.delete_item(10)}")


print("------")
li.print_values()
