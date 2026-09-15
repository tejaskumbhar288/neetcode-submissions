class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build graph
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # 0 = unvisited
        # 1 = currently visiting
        # 2 = completely processed
        state = [0] * numCourses

        def dfs(course):
            # Currently in this DFS path -> cycle
            if state[course] == 1:
                return False

            # Already completely processed -> no cycle
            if state[course] == 2:
                return True

            state[course] = 1 #mark as currently visiting

            # Explore all dependent courses
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # Finished exploring this course
            state[course] = 2

            return True

        # Every course might belong to a different component
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True