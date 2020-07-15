'''
Connected Components
'''

islands=[
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]
islands2 = [
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
]



def island_counter(islands):
    row_count = len(islands)
    col_count = len(islands[0])
    # Create a visited matrix
    visited = []
    for _ in range(row_count):
        visited.append([False] * col_count)
    island_count = 0
    # Walk through each cell of the matrix
    for row in range(row_count):
        for col in range(col_count):
            # If its not been visited
            if not visited[row][col]:
                # If we hit a 1 on the islands
                if islands[row][col] == 1:
                    # Traverse and mark as visited
                    dft(row, col, islands, visited)
                    # increment counter
                    island_count += 1
    return island_count

from utils import Stack
def dft(row, col, islands, visited):
    s = Stack()
    s.push((row, col))
    while s.size() > 0:
        r, c = s.pop()

        if not visited[r][c]:
            visited[r][c] = True

            for neighbor in get_neighbors(r, c, islands):
                s.push(neighbor)


def get_neighbors(row, col, islands):
    neighbors = []
    row_count = len(islands)
    col_count = len(islands[0])
    # check north
    if row > 0 and islands[row-1][col] == 1:
        neighbors.append((row-1, col))
    # check south
    if row < row_count - 1 and islands[row+1][col] == 1:
        neighbors.append((row+1, col))
    # check west
    if col > 0 and islands[row][col-1] == 1:
        neighbors.append((row, col-1))
    # check east
    if col < col_count - 1 and islands[row][col+1] == 1:
        neighbors.append((row, col+1))

    return neighbors

print(island_counter(islands))
print(island_counter(islands2))