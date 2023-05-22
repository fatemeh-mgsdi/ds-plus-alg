# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
           # approach: traverse list and remove next node if its value == val

        # if value matched at head node
        while head and head.val == val:
            head = head.next

        pointer = head
        while pointer and pointer.next:
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        return head