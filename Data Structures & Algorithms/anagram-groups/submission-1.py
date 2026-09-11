class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in grps:
                grps[key]=[]
            grps[key].append(word)
        return list(grps.values())