# same tree
# given the roots of two binary trees, return true if they are the same, and false otherwise

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    # check if both trees are None, if they are, then return true
    if p is None and q is None:
        return True
    # check if one of the trees is None, if it is, return false
    if p is None or q is None:
        return False
    # check if the values of the current nodes are different, if they are, return false
    if p.val != q.val:
        return False
    # recursively call the function on the left and right subtrees
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# test case
if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    result = is_same_tree(p, q)
    print(result)  # Output: True
    if result == True:
        print("Test case passed!")    
    else:
        print("Test case failed!")

    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    p2.right = TreeNode(3)
    q2 = TreeNode(1)
    q2.left = TreeNode(2)
    q2.right = TreeNode(4)

    result2 = is_same_tree(p2, q2)
    print(result2)  # Output: False
    if result2 == False:
        print("Test case passed!")    
    else:        
        print("Test case failed!") 