class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
            

        self.length += 1

    def pop_last(self):
        if self.length == 0:
            return None

        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            

        self.length -= 1
    

    def prepend(self, value):
        new_node = Node(value)

        if self.length ==0 :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1 
    
    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        
        else:
            self.head = self.head.next
            self.head.perv = None
            temp.next = None
        
        self.length -= 1
    
    # Normal get like single linked list
    def get(self, index):
        
        if index >= self.length or index<0:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
    
    # Optimized get using prev
    def optimized_get(self, index):

        if index < self.length/2:
            # index is in first half
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        
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
        before = self.get(index -1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
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
        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        temp.next = None
        temp.prev = None

        self.length -= 1 

        return True



