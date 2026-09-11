from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap=Counter(nums)
        bucket=[[] for _ in range(len(nums)+1)]
        for n, f in freqMap.items():
            bucket[f].append(n)
        res=[]
        for i in range(len(bucket)-1, -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res
        return res