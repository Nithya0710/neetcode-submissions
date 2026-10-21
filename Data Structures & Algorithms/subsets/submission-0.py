class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sets=[]

        def backtrack(i, currSet):
            if i==n:
                sets.append(currSet.copy())
                return
            currSet.append(nums[i])
            backtrack(i+1, currSet)
            currSet.pop()
            backtrack(i+1, currSet)
        
        backtrack(0, [])
        return sets