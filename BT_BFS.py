# Binary Tree BFS (Level Order Traversal)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    # check if the root None, if it is, return an empty list
    if not root:
        return []
    # create a queue to store the nodes we need to visit and an empty
    # list to store the values of the nodes at each level
    queue = deque([root])
    result = []

    # loop until the queue is empty
    while queue:
        # get the number of nodes at the current level
        level_size = len(queue)
        # create an empty list to store the values of the nodes
        # at the current level
        level_values = []
        # process each node at the current level
        for _ in range(level_size):
            # pop the node from the front of the queue and add its value
            # to the level values list
            node = queue.popleft()
            # add the value of the node to the list
            level_values.append(node.val)

            # if the left child exists, add it to the queue
            if node.left:
                queue.append(node.left)
            # if the right child exists, add it to the queue
            if node.right:
                queue.append(node.right)

        # add the values of the current level to the reult list
        result.append(level_values)

    # return the list of values at each level
    return result

# test case
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Call the level_order function and print the result
    print(level_order(root))  # Output: [[3], [9, 20], [15, 7]]
    if level_order(root) == [[3], [9, 20], [15, 7]]:
        print("Test case passed!")    
    else:
        print("Test case failed!")