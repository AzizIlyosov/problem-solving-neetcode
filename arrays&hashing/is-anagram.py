class Solution:
    def counter(self, s):
        s_c = {}
        for i in s:
            if i in s_c:
                s_c[i]+=1
            else:
                s_c[i]=1
        return s_c

    def isAnagram(self, s: str, t: str) -> bool:
        s_c =  self.counter(s)
        t_c =  self.counter(t)

        for t in t_c:
            if t in s_c:
                if t_c[t]!=s_c[t]:
                    return False
            else:
                return False
        
        for s in s_c:
            if s in t_c:
                if t_c[s]!=s_c[s]:
                    return False
            else:
                return False
        
        return True

        