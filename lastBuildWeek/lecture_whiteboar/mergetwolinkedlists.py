# Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists

# examples:
#  Input: 1 -> 2 -> 4, 1 -> 3 -> 4
#  Output: 1 -> 1 -> 2 -> 3 -> -4 -> 4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)


l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(7)

def mergeTwoLists(l1, l2):
    new_list = ListNode(None)
    current_new = new_list
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            current_new.next = ListNode(l1.val)
            l1 = l1.next
        else:
            current_new.next = ListNode(l2.val)
            l2 = l2.next
        current_new = current_new.next
    if l1 is not None:
        current_new.next = l1
    if l2 is not None:
        current_new.next = l2
    return new_list.next
# print(l1)
mergeTwoLists(l1, l2)