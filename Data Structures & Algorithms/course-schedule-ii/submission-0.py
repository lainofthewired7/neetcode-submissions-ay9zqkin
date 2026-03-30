class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        path, coursesAdded = set(), set()

        validOrdering = []

        mapping = defaultdict(list)

        for course in prerequisites:

            mapping[course[0]].append(course[1])

        def dfs(course):

            if course in coursesAdded:

                return True

            if course in path:

                return False

            path.add(course)

            for prereq in mapping[course]:

                if not dfs(prereq):

                    return False

            path.remove(course)
            
            coursesAdded.add(course)

            validOrdering.append(course)

            return True

        for i in range(numCourses):

            if not dfs(i):

                return []

        return validOrdering

            



        