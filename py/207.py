class Solution:
    def getGraph(self, numCourses:int,  prerequisites: list[list[int]]):
        graph = {i:set() for i in range(numCourses)}
        in_degree = {i:0 for i in range(numCourses)}
        for a, b in prerequisites:
            in_degree[a] += 1
            graph[b].add(a)
        
        return graph, in_degree

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if not prerequisites:
            return True

        graph, in_degree = self.getGraph(numCourses, prerequisites)
    
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.appendleft(i)
        
        visited = 0
        while q:
            cur = q.popleft()
            visited += 1

            for neighbor in graph[cur]:
                in_degree[neighbor] -= 1
                
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        if visited == numCourses:
            return True
        return False


        



        

        
