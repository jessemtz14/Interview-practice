# clone graph
# youre given a node in a connected graph
# each node has: 
# val
# neighbors (list of nodes)
# return a deep copy of the graph

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def clone_graph(node):
    # check if the root node is None, if it is, return None
    if not node:
        return None
    
    old_to_new = {} # create a dictionary to map old nodes to new ones
    old_to_new[node] = Node(node.val) # create a new node for the root node and add it to the mapping
    
    queue = deque([node]) # create a queue for BFS and add the root node

    # loop through the graph using BFS
    while queue:
        curr = queue.popleft() # get the current node from the queue

        for neighbor in curr.neighbors: # loop through the neighbors of the current node

            # if the neighbor has not been visited, create a new node for it and add it to the mapping
            if neighbor not in old_to_new:
                old_to_new[neighbor] = Node(neighbor.val)
                queue.append(neighbor) # add the neighbor to the queue for further processing
            # add the new neighbor node to the neighbors list of the current node's new node
            old_to_new[curr].neighbors.append(old_to_new[neighbor])

    return old_to_new[node]


if __name__ == "__main__":
    # Create graph
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    # Clone graph
    cloned = clone_graph(node1)

    # 🔹 Basic structure checks
    print(cloned.val == 1)
    print(sorted([n.val for n in cloned.neighbors]) == [2, 4])

    # 🔹 Check second level neighbors
    n2 = cloned.neighbors[0]
    n4 = cloned.neighbors[1]

    print(sorted([n.val for n in n2.neighbors]) == [1, 3])
    print(sorted([n.val for n in n4.neighbors]) == [1, 3])

    # 🔹 Identity checks (VERY IMPORTANT)
    print(cloned is not node1)  # must be different object
    print(n2 is not node2)
    print(n4 is not node4)

    # 🔹 Deep copy check (no original references)
    print(all(neighbor is not node1 for neighbor in cloned.neighbors))
    print(all(neighbor is not node2 for neighbor in n2.neighbors))

    # 🔹 Final verdict
    if (
        cloned.val == 1 and
        sorted([n.val for n in cloned.neighbors]) == [2, 4] and
        sorted([n.val for n in n2.neighbors]) == [1, 3] and
        sorted([n.val for n in n4.neighbors]) == [1, 3] and
        cloned is not node1 and
        n2 is not node2 and
        n4 is not node4
    ):
        print("✅ Test passed!")
    else:
        print("❌ Test failed!")
    