class Solution:
    def  counter(self, nums):
        c= {}
        for n in nums:
            if n in c:
                c[n]+=1
            else:
                c[n]=1 
        return c
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = self.counter(nums)
        l = [c[i] for i in c]
        l.sort()
        l = l[-k:] 
        return [i for i in c if c[i]>=min(l)  ]