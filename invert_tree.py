# invert tree
# given the root of a binary tree, invert the tree, and return its root

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    # check if the root is none, if it is, return None
    if root is None:
        return None
    # swap the left and right subtrees
    root.left, root.right = root.right, root.left

    # recursively call the function on the left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    # return the root of the iverted tree
    return root

# test case
if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    # print original tree
    print("Original tree:")
    print(root.val)  # Output: 4
    print(root.left.val)  # Output: 2
    print(root.right.val)  # Output: 7
    print(root.left.left.val)  # Output: 1
    print(root.left.right.val)  # Output: 3
    print(root.right.left.val)  # Output: 6
    print(root.right.right.val)  # Output: 9

    result = invert_tree(root)
    print("Inverted tree:")
    print(result.val)  # Output: 4
    print(result.left.val)  # Output: 7
    print(result.right.val)  # Output: 2
    print(result.left.left.val)  # Output: 9
    print(result.left.right.val)  # Output: 6
    print(result.right.left.val)  # Output: 3
    print(result.right.right.val)  # Output: 1

    if result.val == 4 and result.left.val == 7 and result.right.val == 2 and result.left.left.val == 9 and result.left.right.val == 6 and result.right.left.val == 3 and result.right.right.val == 1:
        print("Test case passed!")
    else:
        print("Test case failed!")