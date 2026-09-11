class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold=len(nums)//2
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
            if freq[i]>threshold:
                return i