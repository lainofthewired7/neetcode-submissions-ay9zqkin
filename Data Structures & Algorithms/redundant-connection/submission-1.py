class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj = {i:[] for i in range (1, len(edges)+1)}

        redundant = None

        visited = set()

        def dfs (node, parent):

            if node in visited:

                return False

            visited.add(node)

            for nei in adj[node]:

                if nei == parent:

                    continue

                if not dfs(nei, node):

                    return False

            return True

        for edge in edges:

            adj[edge[0]].append(edge[1])

            adj[edge[1]].append(edge[0])

            if not dfs(edge[0], -1):

                return edge

            visited = set()

        return []
        


        