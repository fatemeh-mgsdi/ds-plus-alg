class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def push(self, value):
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1

    def pop(self):

        if self.height == 0:
            return None
        
        top = self.top
        top.next = None
        
        self.top = self.top.next
        self.height -= 1

        return top.value
        