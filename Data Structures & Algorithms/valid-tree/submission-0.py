class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = {i : [] for i in range (n)}

        path = set()

        visited = set()

        for node1, node2 in edges:

            adj[node1].append(node2)

            adj[node2].append(node1)

        def dfs(node, parent):

            if node in path:

                return False

            path.add(node)

            for neigh in adj[node]:

                if neigh == parent:

                    continue

                if not dfs(neigh, node):

                    return False

            path.remove(node)

            visited.add(node)

            return True

        if not dfs(0, -1):

            return False

        return len(visited) == n




        

        
        