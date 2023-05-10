# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# The successor of a node p is the node with the smallest key greater than p.val.

def inorderSuccessor(root, p):
    if not root:
        return None

    if root.val <= p.val:
        return inorderSuccessor(root.right, p)

    left = inorderSuccessor(root.left, p)
    if not left:
        return root
    else:
        return  left
        