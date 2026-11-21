from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        res=[]
        while queue:
            node=queue.popleft()
            res.append(node)
            for n in graph[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    queue.append(n)
        if len(res)==numCourses:
            return res
        return []