class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        currStart, currEnd=intervals[0]
        for s, e in intervals:
            if currEnd<s:
                res.append([currStart, currEnd])
                currStart, currEnd=s, e
            else:
                currEnd=max(currEnd, e)
        res.append([currStart, currEnd])
        return res