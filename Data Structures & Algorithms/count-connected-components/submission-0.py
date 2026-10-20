class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        adjList=[[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def bfs(node):
            queue=deque([node])
            visited.add(node)
            while queue:
                curr=queue.popleft()
                for neighbor in adjList[curr]:
                    if neighbor not in visited:
                        bfs(neighbor)
                        queue.append(neighbor)
        
        res=0
        for node in range(n):
            if node not in visited:
                res+=1
                bfs(node)
        return res