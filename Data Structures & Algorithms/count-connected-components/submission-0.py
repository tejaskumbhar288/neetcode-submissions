class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. Build the adjacency list.

        # 2. Create a visited set.

        # 3. For every node:
        #     If node hasn't been visited:
        #         Start DFS from that node.
        #         Increment component count.

        # 4. Return component count.

        graph = [[] for _ in range(n)]
        result = 0

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return 

            visited.add(node)

            for next_node in graph[node]:
                dfs(next_node)

        
        for node in range(n):
            if node not in visited:
                dfs(node)
                result += 1


        return result