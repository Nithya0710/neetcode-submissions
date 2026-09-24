class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed):
            total=0
            for pile in piles:
                total+=(pile+speed-1)//speed
            return total<=h
        
        l, r=1, max(piles)
        ans=0
        while l<=r:
            mid=l+(r-l)//2
            if canFinish(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans