class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()    # This will hold edges

    def add_edge(self, fromV, toV):
        if fromV in self.vertices and toV in self.vertices:
            self.vertices[fromV].add(toV)
        else:
            raise IndexError("nonexistent vert")
    
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
