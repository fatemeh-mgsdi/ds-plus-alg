# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
#
# You must solve the problem in O(1) extra space complexity and O(n) time complexity

def oddEvenList(self, head):
    if head:
        odd_tail, cur = head, head.next
        while cur and cur.next:
            even_head = odd_tail.next
            odd_tail.next = cur.next
            odd_tail = odd_tail.next
            cur.next = odd_tail.next
            odd_tail.next = even_head
            cur = cur.next
    return head
