class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freqMap={}
        for c in s:
            if c not in freqMap:
                freqMap[c]=0
            freqMap[c]+=1
        for c in t:
            if c not in freqMap:
                return False
            freqMap[c]-=1
            if freqMap[c]<0:
                return False
        return True