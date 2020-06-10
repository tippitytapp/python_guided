# Linked List
Objective ='''To understand how linked lists work and what some of their pros and cons are'''

# In order to really understand how linked lists work, we'll need to build up a conceptual mental model in our heads and then translate that into code

# Linked Lists store each value as an isolated node

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head_node, tail_node):
        self.head = head_node
        self.tail = tail_node

# How would you insert an element into an empty linked ist?
# How would you interate aong a linked list to reach an element that isnt the head or tail of the list?
# How would you delete an element from a linked list?

# Pros and cons of linked lists
    # Unlike arrays, linked lists do not store elements contiguously.
        # Pro: Easier to insert into and delete from the middle of a linked list compared to an array (Why is this the case?)
        # Con: Linked lists are not as cache-friendly since caches are typically optimized for contiguous memeory accesses
    # Linked LIsts are not to be allocated with the static amount of memory up-front
        # Pro: We can keep adding elements to linked lists as much as we want, unlike arrays with a static amount of allocated memeory