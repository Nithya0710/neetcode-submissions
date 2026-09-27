class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, freqMap, maxFreq=0, {}, 0
        ans=0
        for r in range(len(s)):
            char=s[r]
            freqMap[char]=freqMap.get(char, 0)+1
            maxFreq=max(maxFreq, freqMap[char])
            windowLen=r-l+1
            if windowLen-maxFreq>k:
                freqMap[s[l]]-=1
                l+=1
            ans=max(ans, r-l+1)
        return ans