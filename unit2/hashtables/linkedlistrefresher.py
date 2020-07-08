# head
#  v
# (55) -> (11) -> (22) -> (33) -> (44) -> None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next
        return None # We didn't find it

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def append(self, value):
        node = Node(value)
        cur = self.head
        if cur == None:
            self.head = node
        prev = cur
        cur = cur.next
        if cur == None:
            prev.next = node
        else:
            pass
        

    def delete(self, value):
        cur = self.head
        # SPECIAL CASE - deleting the head
        if cur.value == value:
            self.head = self.head.next
            cur.next = None
            return cur
        # GENERAL CASE - deleting not special cases
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.value == value:
                prev.next = cur.next # cuts out the node from the list
                cur.next = None
                return cur
            else:
                prev = prev.next
                cur = cur.next
        return None # didn't find anything



ll = LinkedList()

ll.insert(11)
ll.insert(22)

# a = Node(11)
# b = Node(22)

# a.next = b

# # (11) -> (22) -> None
# #  ^
# # head
# head = a