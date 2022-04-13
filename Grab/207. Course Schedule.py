'''
    Topological Sort
    Use a 2D-list(adjacency-list) and a 1D list(for in-degree) to store the graph. A queue for Topological Sort.
'''

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        # edge[1] -> edge[0]
        for edge in prerequisites:
            indegree[edge[0]] += 1
            adj[edge[1]].append(edge[0])
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        nodeleft = numCourses
        while queue:
            cur = queue.popleft()
            nodeleft -= 1
            for node in adj[cur]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        
        return nodeleft == 0
            
