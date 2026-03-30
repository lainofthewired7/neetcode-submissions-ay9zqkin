class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mapping = defaultdict(list)

        path = set()

        visited = set()

        def dfs(node):

            if node in visited:

                return False

            if node in path:

                return True

            path.add(node)

            cycleDetected = False

            for neighbor in mapping[node]:

                if dfs(neighbor):

                    return True

            visited.add(node)

            path.remove(node)

            return False


        for prereq in prerequisites:

            if prereq[0] == prereq[1]:
                
                return False

            mapping[prereq[0]].append(prereq[1])

        cycleDetected = False

        for node in range (numCourses):

            if dfs(node):

                return False


        return True