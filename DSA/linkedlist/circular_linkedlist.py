class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last = None):
        self.last = last
        
    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.last = new_node
            new_node.next = self.last
        else:
            temp = self.last
            new_node.next = temp.next
            temp.next = new_node
            
    def insert_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.last = new_node
            new_node.next = self.last
        else:
            temp = self.last
            new_node.next = temp.next
            temp.next = new_node
            self.last = new_node
    
    def search(self, data):
        if not self.is_empty():
            temp = self.last.next
            if temp == self.last:
                if temp.item == data:
                    return temp
            else:
                while temp:
                    if temp.item == data:
                        return temp
                    temp = temp.next
                    if temp == self.last.next:
                        break
        return None 

    def insert_after(self, temp, data):
        if temp:
            new_node = Node(data, temp.next)
            temp.next = new_node
            if temp == self.last:
                self.last = new_node
            return new_node
        return None
    
    def print_values(self):
        temp = self.last.next
        while temp:
            print(temp.item)
            temp = temp.next
            if temp == self.last.next:
                break

    def delete_first(self):
        if not self.is_empty():
            if self.last == self.last.next:
                self.last = None
            else:
                self.last.next = self.last.next.next
                
    def delete_last(self):
        if not self.is_empty():
            if self.last == self.last.next:
                self.last = None
            else:
                temp = self.last
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp  
                
    def delete_item(self, data):
        if not self.is_empty():
            if self.last == self.last.next:
                if self.last.item == data: 
                    self.last = None
            else:
                temp = self.last.next
                if temp.item == data:
                    self.last.next = temp.next
                else:
                    while temp.next:
                        if temp.next.item == data:
                            if temp.next == self.last:
                                self.last = temp
                            temp.next = temp.next.next
                            return temp
                        else:
                            temp = temp.next
                        if temp == self.last.next:
                            break 
                        
    def __iter__(self):
        if not self.last:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)  


class CLLIterator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.flag = False
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration 
        if self.current == self.start and self.flag == True:
            raise StopIteration
        else:
            self.flag = True
                 
        data = self.current.item
        self.current = self.current.next
        return data
    
    
cll = CLL()
cll.insert_at_last(20)
cll.insert_at_start(10)
cll.insert_at_last(40)
cll.insert_after(cll.search(20),30)
cll.insert_at_last(50)

# cll.delete_first()
# cll.delete_last()
# cll.delete_item(30)

# cll.print_values()

for val in cll:
    print(val)
    
