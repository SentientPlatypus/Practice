class Solution:
    def make_graph(self, n, relations: List[List[int]]):
            res = {i: set() for i in range(1, n + 1)}
            for p, next_node in relations:
                res[p].add(next_node)
            return res

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = self.make_graph(n, relations)
        in_degree = {k: 0 for k in graph.keys()}

        for node in range(1, n + 1):
            neighbors = graph[node]
            for nbr in neighbors:
                in_degree[nbr] += 1

        base_courses = [node for node in in_degree.keys() if in_degree[node] == 0]

        q = deque(base_courses) #invariant for q is that everything in q has no prereqs that have not been processed already
        dp = [0] + time

        while q:
            cur = q.popleft()

            neighbors = graph[cur]
            for nbr in neighbors:
                dp[nbr] = max(dp[nbr], dp[cur] + time[nbr - 1])

                in_degree[nbr] -= 1
                if in_degree[nbr] == 0:
                    q.append(nbr)
        return max(dp)


        

class Solution:
    def build_graph(self, n:int, relations:List[List[int]]):
        g = {node:set() for node in range(1, n + 1)}

        for prereq, postreq in relations:
            g[prereq].add(postreq)
        
        return g

    def M(self, graph, root, time:List[int], memo):
        "M(root) is the longest path in the graph that starts at i"
        if root in memo:
            return memo[root]

        longestPath = 0
        for neighbor in graph[root]:
            longestPath = max(longestPath, self.M(graph, neighbor, time, memo))
        
        memo[root] = longestPath + time[root - 1]
        
        return memo[root]

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        res = 0

        graph = self.build_graph(n, relations)
        memo = {} #stores longestPaths starting from a node.

        for root in range(1, n + 1):
            res = max(res, self.M(graph, root, time, memo))
        return res
