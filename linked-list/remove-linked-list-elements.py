# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(self, head, val):
    if head is None:
        return None

    while head.val == val:
        head = head.next
        if not head:
            return None

    new_head = ListNode(head.val)

    cur = head.next
    pre = new_head

    while cur:
        if cur.val != val:
            new_node = ListNode(cur.val)

            pre.next = new_node
            pre = new_node

        cur = cur.next

    return new_head



