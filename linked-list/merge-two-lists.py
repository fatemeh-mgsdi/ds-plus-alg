class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
    head = new_list = ListNode(0)

    while (list1 and list2):
        if (list1.val < list2.val):
            new_list.next = list1
            list1 = list1.next
        else:
            new_list.next = list2
            list2 = list2.next
        new_list = new_list.next

    new_list.next = list1 or list2
    return head.next
