class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]

        def backtrack(pos, currSet, runningSum):
            if runningSum==target:
                res.append(currSet.copy())
                return
            for i in range(pos, len(candidates)):
                if i>pos and candidates[i-1]==candidates[i]:
                    continue
                if runningSum+candidates[i]>target:
                    break
                currSet.append(candidates[i])
                runningSum+=candidates[i]
                backtrack(i+1, currSet, runningSum)
                currSet.pop()
                runningSum-=candidates[i]

        backtrack(0, [], 0)
        return res