class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build a graph
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # 0 = unvisited
        # 1 = currently visiting
        # 2 = completely processed
        states = [0] * numCourses

        def dfs(course):
            #if it is in current visiting -> cycle
            if states[course] == 1:
                return False

            #if it is completely processed -> no cycle
            if states[course] == 2:
                return True

            states[course] = 1 # mark it as currently visiting

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            #mark it as completely processed
            states[course] = 2

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
