class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used=set()
        l, maxLen=0, 0
        for r in range(len(s)):
            while s[r] in used:
                used.remove(s[l])
                l+=1
            used.add(s[r])
            maxLen=max(maxLen, r-l+1)
        return maxLen