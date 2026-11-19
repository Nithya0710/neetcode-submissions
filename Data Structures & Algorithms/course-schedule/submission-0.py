from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        queue=deque()
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        res=0
        while queue:
            node=queue.popleft()
            res+=1
            for n in graph[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    queue.append(n)
        return res==numCourses