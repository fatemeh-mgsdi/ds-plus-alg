# Given the head of a linked list, remove the nth node from the end of the list and return its head.

def deleteNthNodeFromEnd(self, head, n):
    fast = head
    slow = head

    for _ in range(n):
        fast = fast.next

    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head