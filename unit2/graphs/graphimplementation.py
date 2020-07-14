# Graph Implementation
# Nodes connected by Edges

from utils import  * 

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

    def bft(self, vertex_id):
        # create an empty queue
        q = Queue()
        # create an empty set to store the visited nodes
        visited = set()
        # init: enqueue the starting node
        q.enqueue(vertex_id)
        # While the queue isn't empty
        while q.size() > 0:
            # dequeue the first item
            v = q.dequeue()
            # if its not been visited:
            if v not in visited:
                # Mark as visited i.e. add to the visited
                visited.add(v)
                # Do something with the node
                print(f'Visited BFT {v}')
                # Add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
    
    def dft(self, vertex_id):
        # create an empty stack
        s = Stack()
        # create an empty set to store the visted nodes
        visited = set()
        # init: add the starting node to the stack
        s.push(vertex_id)
        # while the stack is not empty
        while s.size() > 0:
            # pop the first item
            v = s.pop()
            # if its not been visited
            if v not in visited:
                # add to the visited set
                visited.add(v)
                # do something with the node
                print(f'Visited DFT {v}')
                # add all nieghbors to the stack
                for next_v in self.get_neighbors(v):
                    s.push(next_v)

    # whenever you think fasted path, think of BFT
    def bft_search(self, start, target):
        # create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        # Create a Set to store visited vertices
        visited = set()
        q.enqueue([start])
        # WHile the queue is not empty
        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == target:
                    return path
                visited.add(vertex)
                for next_v in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_v)
                    q.enqueue(new_path)
        return f'sorry bout it'


graphy = Graph()

graphy.add_vertex('A')
graphy.add_vertex('B')
graphy.add_vertex('C')
graphy.add_vertex('D')
graphy.add_edge('A', 'B')
graphy.add_edge('A', 'C')
graphy.add_edge('B', 'A')
graphy.add_edge('B', 'B')
graphy.add_edge('B', 'C')
graphy.add_edge('C', 'D')
graphy.add_edge('D', 'C')

# print("A", graphy.get_neighbors('A'))
# print("B", graphy.get_neighbors('B'))
# print("C", graphy.get_neighbors('C'))

# print("Graphy", graphy.vertices)
graphy.bft('B')
graphy.dft('B')
# ll = Graph()

# ll.add_vertex('X')
# ll.add_vertex('Y')
# ll.add_vertex('Z')

# ll.add_edge('X', 'Y')
# ll.add_edge('Y', 'Z')

# print("LL", ll.vertices)