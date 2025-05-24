# Detect Cycle in Linked List
# Problem: Determine if a linked list has a cycle.

# Concepts: Two-pointer (Floyd’s cycle-finding algorithm).

def detectCycle(head):
    slow=fast=head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# Creating a cycle for testing
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creating a cycle (4 -> 2)
result = detectCycle(node1)
print(result)  # Output: True