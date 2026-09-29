import math

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) or t=='':
            return ""
        freqMap=Counter(t)
        windowFreq=defaultdict(int)
        matches, bestLen, bestL=0, math.inf, 0
        l=0
        for r in range(len(s)):
            c=s[r]
            if c in freqMap:
                windowFreq[c]+=1
                if windowFreq[c]==freqMap[c]:
                    matches+=1
            while matches==len(freqMap):
                if bestLen>(r-l+1):
                    bestLen=r-l+1
                    bestL=l
                c=s[l]
                if c in freqMap:
                    windowFreq[c]-=1
                    if windowFreq[c]<freqMap[c]:
                        matches-=1
                l+=1
        if bestLen==math.inf:
            return ""
        return s[bestL:bestLen+bestL]