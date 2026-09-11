class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        store=set(nums)
        for i in nums:
            streak,curr=0,i
            while curr in store:
                streak+=1
                curr+=1
            res=max(res,streak)
        return res