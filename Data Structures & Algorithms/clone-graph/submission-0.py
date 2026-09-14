"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(node):
            #first check if clone already created
            if node in old_to_new:
                return old_to_new[node]

            #if not created then first create a clone
            clone = Node(node.val)

            #store the clone before visiting its neighbours
            old_to_new[node] = clone

            for neighbour in node.neighbors:
                clone.neighbors.append(dfs(neighbour))

            return clone

        return dfs(node)

            
