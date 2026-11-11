import heapq

from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap=Counter(tasks)
        heap=[(-f, t) for t,f in freqMap.items()]
        heapq.heapify(heap)
        queue=deque()
        currTime=0
        while heap or queue:
            currTime+=1
            if queue and queue[0][2]==currTime:
                task=queue.popleft()
                heapq.heappush(heap, (task[0], task[1]))
            if heap:
                f, t=heapq.heappop(heap)
                f+=1
                if f<0:
                    queue.append((f, t, currTime+n+1))
        # if heap or queue:
        #     return -1
        return currTime