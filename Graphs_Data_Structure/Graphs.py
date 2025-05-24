

class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []
        
    def __str__(self):
        return f'Node({self.value})'
    
    def display(self):
        connections = [node.value for node in self.neighbors]
        return f'{self.value} is Connected to {connections}'
    

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

A.neighbors.append(B)
B.neighbors.append(A)

C.neighbors.append(D)
D.neighbors.append(C)

print(B.display())


# Array of Edges (Directed) [Start, End]

n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Convert Array of Edges -> Adjacency Matrix

M = []
for i in range(n):
    M.append([0]*n)
    
for u, v in A:
    # print(u,v)
    M[u][v] = 1
    
    # Uncomment the following line if the graph is undirected
    # M[v][u] = 1
    
print(M)


# Convert Array of Edges -> Adjacency List
from collections import defaultdict

D = defaultdict(list)

for u,v in A:
    D[u].append(v)
    
    # Uncomment the following line if the graph is undirected
    # D[v].append(u)
    
print(D)
print(D[3])


# DFS with Recursion - O(V + E) where V is the number of nodes and E is the number of edges

seen = set()
source = 0
seen.add(source)

def DFS(Node):
    print(Node)
    for neigbor in D[Node]:
        if neigbor not in seen:
            seen.add(neigbor)
            DFS(neigbor)
            
            
DFS(source)         \
    

# BFS (Queue) - O(V + E)

from collections import deque

source = 0
seen = set()
seen.add(source)
q = deque()
q.append(source)


while q:
    node = q.popleft()
    print(node)
    for neighbor in D[node]:
        if neighbor not in seen:
            seen.add(neighbor)
            q.append(neighbor)
        
        

 