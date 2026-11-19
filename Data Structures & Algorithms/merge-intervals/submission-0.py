class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        maxVal=max(interval[0] for interval in intervals)
        mp=[0]*(maxVal+1)
        for start, end in intervals:
            mp[start]=max(end+1, mp[start])
        res=[]
        have=-1
        intStart=-1
        for i in range(len(mp)):
            if mp[i]!=0:
                if intStart==-1:
                    intStart=i
                have=max(mp[i]-1, have)
            if have==i:
                res.append([intStart, have])
                have=-1
                intStart=-1
        if intStart!=-1:
            res.append([intStart, have])
        return res