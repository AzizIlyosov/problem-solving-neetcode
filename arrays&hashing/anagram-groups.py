class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key=list(s )
            key.sort()
            key = ''.join(key)
            if key in d: 
                d[key].append(s)
            else:
                d[key]=[s,]

        return [d[i] for i in d]
