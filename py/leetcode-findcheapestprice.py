class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        
        def construct_graph_from_list(flights: list[list[int]]):
            graph = {}
            for s, d, c in flights:

                if s in graph.keys():
                    graph[s][d] = c
                else:
                    graph[s] = {d:c}
                if d in graph.keys():
                    continue
                else:
                    graph[d] = {}
            return graph

        graph = construct_graph_from_list(flights)
        print(graph)
        
        ##BFS

        total_d = {}
        q = []
        q.append(src)
        total_d[src] = 0


        for layer in range(k + 1):
            print(q)
            nq = []
            while q:
                current = q.pop(0)

                for node in graph[current].keys():
                    nq.append(node)

                    if node in total_d.keys():
                        total_d[node] = min(total_d[node], total_d[current] + graph[current][node])
                    else:
                        total_d[node] = total_d[current] + graph[current][node]
            q = nq
        
        if dst in total_d:
            return total_d[dst]
        return -1



print(
    Solution.findCheapestPrice(
        Solution(),
        n=4,
        flights=[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
        src = 0,
        dst=3,
        k=1
    )
)
