#Binary Tree or Binary Search Tree

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.content = None

    def insert(self, value, content = None):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = TreeNode(value)
                self.right.content = content
            else:
                self.right.insert(value, content)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(f"Inorder Traversal:",self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(f"Preorder Traversal:",self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(f"Postorder Traversal:",self.value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.find(value)
        else:
            return self


tree = TreeNode(10)
tree.insert(4)
tree.insert(6)
tree.insert(2, {"data": "Hello World!"})
tree.insert(17)
tree.insert(30)
tree.insert(35)
tree.insert(16)

# print(tree.left.left.value)
# print(tree.right.right.right.value)
tree.inorder_traversal()
tree.preorder_traversal()
tree.postorder_traversal()

print(tree.find(2).content["data"])
