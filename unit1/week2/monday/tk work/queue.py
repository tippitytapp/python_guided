# Queue Data Structure

Objective = '''To understand how queues work and what some of their pros and cons are.'''

# in order to really understand how queues work, we'll need to build up a conceptual mental model in our heads and then translate that model into code

# Encapsulates ordering... AKA waiting in line

FIFO = 'First in first out'

class Queue:
    def __init__(self, storage_data_structure):
        self.size = 0
        self.storage = storage_data_structure

# Questions to ask yourself:

    # Whats the opposite of FIFO ordering? What data structures exhibit its ordering
    # What data structures would you use to implement a queue
    # When is FIFO ordering useful? When is it not

# Pros and Cons:

    # Pro: Queues are simple and intuitive to use and implement
    # Pro: They can be used to serialize data coming in from multipe sources
    # Con: Are not general-purpose at all in and of themselves