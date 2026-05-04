# max_depth_BT.py
# Maximum depth of a binary tree
# given the root of a BT, return its max depth
# depth = number of nodes from the root

#example:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# depth at a node is 1 + max depth of its left and right subtrees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    # check if the root if None, if it is, return 0
    if root is None:
        return 0
    
    # recursively call the function on the left and right subtrees
    left = max_depth(root.left)
    right = max_depth(root.right)
    # return the max depth
    return max(left, right) + 1

# test case
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = max_depth(root)
    print(result)  # Output: 3
    if result == 3:
        print("Test case passed!")    
    else:
        print("Test case failed!")
