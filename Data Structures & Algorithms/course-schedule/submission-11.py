class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range (numCourses)}

        for prereq in prerequisites:

            adj[prereq[0]].append(prereq[1])

        seen = set()

        path = set()

        def dfs(course):

            if course in seen:

                return True

            if course in path:

                return False

            path.add(course)

            for neigh in adj[course]:

                if not dfs(neigh):

                    return False

            seen.add(course)

            return True

        for i in range (numCourses):

            path = set()

            if not dfs(i):

                return False

        return True


        