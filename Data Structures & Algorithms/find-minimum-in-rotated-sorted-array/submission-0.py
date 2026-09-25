class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r=0, len(nums)-1
        minEle=nums[l]
        while l<=r:
            mid=l+(r-l)//2
            if nums[l]<=nums[r]:
                minEle=min(minEle, nums[l])
                break
            if nums[l]<=nums[mid]:  # left half sorted
                minEle=min(minEle, nums[l])
                l=mid+1
            else:   # right half sorted
                minEle=min(minEle, nums[mid])
                r=mid-1
        return minEle