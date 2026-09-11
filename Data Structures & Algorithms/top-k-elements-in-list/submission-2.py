import heapq

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap=Counter(nums)
        heap=[]
        for n, f in freqMap.items():
            heapq.heappush(heap, (-f, n))
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res