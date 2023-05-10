# Tree

- Linked list is actually a form of a tree 
- In a binary tree, a Full one is one which every node either points to zero nodes or two nodes or two nodes
- With a perfect tree, any level in the tree that has any nodes is completed all the way across.
- With a complete tree, you are filling the tree from left to right with no gaps
- A perfect tree is always complete, but it's not true in the other way
- Binary tree is not a Binary Search Tree


# Binary Search Tree
- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- The left and right subtree each must also be a binary search tree.

## Big O

Number of nodes = 2**n - 1 (n is level) 
ps: Read it like this: 
2**2 -1 => two to the two minus one
2**3 - 1=> two to the three minus one
....

Fot lookup, insert and remove
If the binary search tree is a straight line, then it is just like a linked list=> searching for a node is O(n). But, usually we ignore this case and treat it as if it is O(logn).


