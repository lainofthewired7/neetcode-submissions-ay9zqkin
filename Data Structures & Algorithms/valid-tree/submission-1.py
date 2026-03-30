class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:

            return False

        adj = {i : [] for i in range (n)}

        visited = set()

        for node1, node2 in edges:

            adj[node1].append(node2)

            adj[node2].append(node1)

        def dfs(node, parent):

            if node in visited:

                return False

            visited.add(node)

            for neigh in adj[node]:

                if neigh == parent:

                    continue

                if not dfs(neigh, node):

                    return False
                    

            return True

        if not dfs(0, -1):

            return False

        return len(visited) == n




        

        
        