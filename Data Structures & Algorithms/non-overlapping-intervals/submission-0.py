class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        lastEnd=intervals[0][1]
        removals=0
        for interval in intervals[1:]:
            currStart, currEnd=interval[0], interval[1]
            if currStart<lastEnd:
                removals+=1
            else:
                lastEnd=currEnd
        return removals