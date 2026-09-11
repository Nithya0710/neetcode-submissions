class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes=[len(s) for s in strs]
        res=[]
        for size in sizes:
            res.append(str(size))
            res.append(',')
        res.append('#')
        for word in strs:
            for c in word:
                res.append(c)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes=[]
        i=0
        while i<len(s):
            if s[i]=='#':
                j=i
                break
            if s[i]==',':
                i+=1
                continue
            num=[]
            while s[i]!=',':
                num.append(s[i])
                i+=1
            sizes.append(int("".join(num)))
        res=[]
        j+=1
        for size in sizes:
            word=[]
            for i in range(size):
                word.append(s[j])
                j+=1
            res.append("".join(word))
        return res   