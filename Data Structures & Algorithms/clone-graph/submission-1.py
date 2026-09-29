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
            #if node is already present
            if node in old_to_new:
                return old_to_new[node]

            #if not then create a clone
            clone = Node(node.val)

            #save it before visiting the neighbors
            old_to_new[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

            
        return dfs(node)

        