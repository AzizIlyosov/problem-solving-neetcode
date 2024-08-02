class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ns = set(nums)
        l=[]
        if len(nums)==0:
            return 0

        for n in ns:
            l.append([])

            while(True) :
                if n+1 in ns:
                    l[-1].append(n+1)
                    n=n+1
                else: 
                    break 
                    
        m = max([len(i) for i in l])
        return m+1
         