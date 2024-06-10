class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
       
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def postorder_traversal(self):
        
        return self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        
        nodes = []
        if node:
            nodes.extend(self._postorder_recursive(node.left))
            nodes.extend(self._postorder_recursive(node.right))
            nodes.append(node.value)
        return nodes


bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)
bt.insert(12)
bt.insert(18)

# Traversal postorder
print("Postorder Traversal:", bt.postorder_traversal())  # Output: [3, 7, 5, 12, 18, 15, 10]