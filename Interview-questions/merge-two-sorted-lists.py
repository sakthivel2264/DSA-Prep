# Merge Two Sorted Lists
# Problem: Merge two sorted linked lists into one sorted list.

# Concepts: Linked lists, pointers.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next
    
    def mergeTwolists(self, l1, l2):
        dummy = Node()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy.next
    

# Example usage
l1 = Node(1, Node(2, Node(4)))
l2 = Node(1, Node(3, Node(4)))
result = l1.mergeTwolists(l1, l2)
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")

# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None