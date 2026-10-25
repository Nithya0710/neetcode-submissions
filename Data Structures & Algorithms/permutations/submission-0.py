class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def backtrack(pos):
            if pos==len(nums):
                res.append(nums.copy())
                return
            for i in range(pos, len(nums)):
                nums[pos], nums[i]=nums[i], nums[pos]
                backtrack(pos+1)
                nums[pos], nums[i]=nums[i], nums[pos]
        
        backtrack(0)
        return res