# The important thing to note is, inorder successor is needed only when the right child is not empty.

class Node:

    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def deleteNode(self,root, key):

        # Base Case
        if root is None:
            return root

        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if key < root.key:
            root.left = self.deleteNode(root.left, key)

        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif (key > root.key):
            root.right = self.deleteNode(root.right, key)

        # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.get_min(root.right)

            # Copy the inorder successor's
            # content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.key)

        return root
