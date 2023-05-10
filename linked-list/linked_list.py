# Linked list is actually a form of a tree 


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head =new_node
        self.tail = new_node
        self.length = 1

    
    def append(self, value):
        new_node = Node(value)

        if not self.head: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop_last(self):
        if self.length == 0:
            return None

        current = self.head
        while current.next:
            current = current.next
        self.tail = current
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
    

    def prepend(self, value):
        new_node = Node(value)

        if self.length ==0 :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1 
    
    def pop_first(self):
        if self.length == 0:
            return None

        current = self.head
        self.head = self.head.next
        current.next = None

        self.length -= 1
        if self.length == 0:
            self.tail = None
        
        return current.value
    
    def get(self, index):
        
        if index >= self.length or index<0:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
    
    def set(self, index, value):
        
        temp = self.get(index)
        if temp:
            temp.value = value

    def insert(self, index, value):
        if index >= self.length or index<0:
            return None
        if index == 0 :
            return self.prepend(value)
        
        if index == self.length :
            return self.append(value)

        new_node = Node(value)

        temp = self.get(index-1)

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1 

        return True
    
    def remove(self, index):
        if index >= self.length or index<0:
            return None
        
        if index == 0 :
            return self.pop_first(index)
        
        if index == self.length :
            return self.pop_last(index)
        
        temp = self.get(index-1)
        temp.next = temp.next.next

        self.length -= 1 

        return True



