from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Kahn's algorithm
        #buid a graph
        graph = [[] for _ in range(numCourses)]

        # Number of prerequisites for each course
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        result = []

        # Courses that have no prerequisites
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()

            result.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

            
         # If we couldn't process every course,
        # there must be a cycle.
        if len(result) != numCourses:
            return []

        return result