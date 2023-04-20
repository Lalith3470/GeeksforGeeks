from typing import List

class Solution:
    def reverse(self,st): 
        #code here
        def rev(idx,st,N):
            if idx>=N//2:
                return
            st[idx],st[N-idx-1]=st[N-idx-1],st[idx]
            rev(idx+1,st,N)
        rev(0,st,len(st))
        return st
        
