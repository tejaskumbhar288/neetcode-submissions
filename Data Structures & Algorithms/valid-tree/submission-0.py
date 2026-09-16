class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have n - 1 edges
        if len(edges) != (n-1):
            return False

        #build a graph
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)

            for next_node in graph[node]:
                dfs(next_node)

        #every not should be reachable from 0
        dfs(0)

        return len(visited) == n

