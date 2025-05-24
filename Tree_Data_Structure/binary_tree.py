

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.value)
    
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

# print(A)
   
# Depth First Search   
   
# Traverse        
# Node
# Left
# Right
        
def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)
    
print("PreOrder Traversal:")    
pre_order(A)

# Traverse
# Left
# Node
# Right
def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)
    
print("InOrder Traversal:")    
in_order(A)

# Traverse
# Left
# Right
# Node
def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)
    
print("PostOrder Traversal:")
post_order(A)



#Breath First Search or level Order Traversal

from collections import deque

def BFS(node):
    q = deque()
    q.append(node)
    
    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
        
print("Breath First Search or level Order Traversal:")        
BFS(A)        

# recursive Find
def find(node, target):
    if not node:
        return
    
    if target == node.value:
        return True
    else: return find(node.left, target) or find(node.right, target)
    
    
print(find(A, 4)) # True