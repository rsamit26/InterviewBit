"""
Binary Tree Implementation
--------------------------
Tree Node:
        - left child
        - right child
        - data (Value of that Node)

------------ Methods ------------

1. Get ::
        Returns the value of Root node
2. Set ::
        Set the value of Root Node
3. Insert ::
        Insert a new node in the tree
4. Search ::
        Search a key in the tree and returns the node and the parent node
5. Remove ::
        Remove a key from the tree and returns a binary search tree



"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get(self):
        return self.data

    def set(self, data):
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, key, parent=None):

        if key < self.data:
            if self.left is None:
                return str(key) + "Not found in tree "
            return self.left.search(key, self)
        elif key > self.data:
            if self.right is None:
                return str(key) + "Not found in tree "
            return self.right.search(key, self)
        else:
            return self, parent

    def child_count(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def remove(self, key):

        node, parent = self.search(key)
        if node is not None:
            child_count = node.child_count()
            if child_count == 0:
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.data = None
            elif child_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data

                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def tree_traversal(self):
        if self.left:
            self.left.tree_traversal()
        print(self.data)
        if self.right:
            self.right.tree_traversal()


# """Testing code"""
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.tree_traversal()
# node, parent = root.search(6)
# print(node.data, parent.data)
# root.remove(6)
# root.tree_traversal()
