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

            return

        mapping = {}

        def dfs(node):

            if node in mapping:

                return

            newNode = Node(node.val, [])

            mapping[node] = newNode

            for neighbor in node.neighbors:

                newNeighbor = dfs(neighbor)

                if newNeighbor:

                    newNode.neighbors.append(newNeighbor)

                else:

                    newNode.neighbors.append(mapping[neighbor])

            return newNode

        return dfs(node)

            