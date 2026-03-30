class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range (n)}

        visited = set()

        numComponents = 0

        for vertex1, vertex2 in edges:

            adj[vertex1].append(vertex2)

            adj[vertex2].append(vertex1)


        def dfs(node):

            if node in visited:

                return

            visited.add(node)

            for nei in adj[node]:

                dfs(nei)

        
        for i in range (n):

            if i in visited:
                continue

            dfs(i)

            numComponents += 1

        return numComponents

        

        

        

            


        