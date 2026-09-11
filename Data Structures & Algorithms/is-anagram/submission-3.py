from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1=Counter(s)
        f2=Counter(t)
        sorted(f1)
        sorted(f2)
        return f1==f2