class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def backtrack(start, currSet):
            res.append(currSet.copy())
            for i in range(start, len(nums)):
                if i!=start and nums[i]==nums[i-1]:
                    continue
                currSet.append(nums[i])
                backtrack(i+1, currSet)
                currSet.pop()
        
        backtrack(0, [])
        return res