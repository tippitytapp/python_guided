class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head):
    visited = set()
    if head.next is None:
        return False
    while head.next is not None:
        visited.add(head)
        if head.next in visited:
            return True
        self.hasCycle(head.next)

    current = head
    while current is not None:
        if hasattr(current, 'visited'):
            return True
        current.visited = True
        current = current.next
    return False