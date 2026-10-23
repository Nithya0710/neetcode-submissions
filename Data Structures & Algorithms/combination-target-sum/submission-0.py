class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def backtrack(pos, curr, runningSum):
            if runningSum==target:
                res.append(curr.copy())
                return 
            elif runningSum>target:
                return
            for i in range(pos, len(nums)):
                curr.append(nums[i])
                runningSum+=nums[i]
                backtrack(i, curr, runningSum)
                curr.pop()
                runningSum-=nums[i]
        
        backtrack(0, [], 0)
        return res