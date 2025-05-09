
class SinglyNode:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)
    
head = SinglyNode(1)
a = SinglyNode(2)
b = SinglyNode(3)
c = SinglyNode(4)

head.next = a
a.next = b
b.next = c
c.next = None

print(b.next)

# Traversal of Singly Linked List

def traverse(head):

    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

traverse(head)

# Inserting a node at the end of the linked list

def insert_at_end(head, data):
    new_node = SinglyNode(data)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

insert_at_end(head, 5)
traverse(head)

# Inserting a node at the beginning of the linked list

def insert_at_beginning(head, data):
    new_node = SinglyNode(data)
    new_node.next = head
    return new_node

head = insert_at_beginning(head, 0)
traverse(head)

# Inserting a node at a specific position in the linked list

def insert_at_position(head, data, position):
    new_node = SinglyNode(data)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    for _ in range(position - 1):
        if current is None:
            raise Exception("Position out of bounds")
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

head = insert_at_position(head, 4.5, 5)
traverse(head)

#  Searching for a node in the linked list

def search(head, key):
    current = head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False
    
    
print(search(head, 3))  # True
print(search(head, 10))  # False