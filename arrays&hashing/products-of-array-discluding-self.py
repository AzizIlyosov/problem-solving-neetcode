class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        forward = [1,]
        for n in nums[:-1]:
            forward.append(n*forward[-1])
        
        dd= nums[::-1]
        backward=[1,]
        for d in dd[:-1]:
            backward.append(backward[-1]*d) 
        backward = backward[::-1] 


        return [i*j for i,j in zip(forward,backward)]