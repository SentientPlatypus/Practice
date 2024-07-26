import heapq


#n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]],
class Solution:
    def dijkstra(start, graph, n):
        dist = [float('inf')] * n
        dist[start] = 0
        pq = [(0, start)]

        while pq:
            currentDist, u = heapq.heappop(pq)

            if currentDist > dist[u]:
                continue

            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        return dist

    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        # Create the graph as an adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        minReachableCities = float('inf')
        city = -1

        for i in range(n):
            dist = Solution.dijkstra(i, graph, n)
            reachableCities = sum(d <= distanceThreshold for d in dist)

            if reachableCities <= minReachableCities:
                minReachableCities = reachableCities
                city = i

        return city