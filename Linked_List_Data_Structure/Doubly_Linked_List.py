class DoublyNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)

# Build initial list manually or You can Insert Using functions below
head = tail = DoublyNode(0)
# a = DoublyNode(1)
# b = DoublyNode(2)
# c = DoublyNode(3)
# d = DoublyNode(4)

# Link the nodes
# head.next = a
# a.prev = head
# a.next = b
# b.prev = a
# b.next = c
# c.prev = b
# c.next = d
# d.prev = c

# tail = d 

# print(head.next.next.next.prev)

# Traversal
def traverse(head):
    while head:
        print(head.data, end=" <-> ")
        head = head.next
    print(head)

traverse(head)

# Insert at end
def insert_at_end(head, tail, val):
    if head is None and tail is None:
        head = tail = DoublyNode(val)
        return head, tail
    else:
        new_node = DoublyNode(val, prev=tail)
        tail.next = new_node
        return head, new_node 

# Insertion
head, tail = insert_at_end(head, tail, 5)
traverse(head)


print(tail)


# Inserting a node at the beginning of the linked list

def insert_at_begin(head, val):
    if head == None:
        head = DoublyNode(val)
        return head
    else:
        new_node = DoublyNode(val, next=head)
        head.prev = new_node
        return new_node

head = insert_at_begin(head, 0.5)

traverse(head)

print(head)