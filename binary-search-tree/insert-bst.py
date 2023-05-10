from typing import Optional


# If the node  doesn’t yet have a value, we can just set the given valune and return. if we ever
# try to insert a value that also exists, we can also simply return as this can be considered a noop.
# If the given value is less than our node’s value and we already have a left child then
# we recursively call insert on our left child.If we don’t have a left child yet then we just make the
# given value our new left child.We can do the same (but inverted) for our right side.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

