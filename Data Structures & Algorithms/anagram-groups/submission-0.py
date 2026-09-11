class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            sortedStr=''.join(sorted(i))
            res[sortedStr].append(i)
        return list(res.values())
