import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2=nums2, nums1
        m, n=len(nums1), len(nums2)
        l, r=0, m
        totalLeft=(m+n+1)//2
        while l<=r:
            part1=(l+r)//2
            part2=totalLeft-part1
            if part1==0:
                l1=-math.inf
            else:
                l1=nums1[part1-1]
            if part1==m:
                r1=math.inf
            else:
                r1=nums1[part1]
            if part2==0:
                l2=-math.inf
            else:
                l2=nums2[part2-1]
            if part2==n:
                r2=math.inf
            else:
                r2=nums2[part2]
            if l1<=r2 and l2<=r1:
                if (m+n)%2==1:
                    return float(max(l1, l2))
                maxLeft=max(l1, l2)
                minRight=min(r1, r2)
                return (maxLeft+minRight)/2
            elif l1>r2:
                r=part1-1
            else:
                l=part1+1