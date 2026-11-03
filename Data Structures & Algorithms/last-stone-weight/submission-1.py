import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heap.append(-stone)
        heapq.heapify(heap)
        while len(heap)>1:
            y=-heapq.heappop(heap)
            x=-heapq.heappop(heap)
            if x<y:
                heapq.heappush(heap, x-y)
        heap.append(0)
        return -heap[0]