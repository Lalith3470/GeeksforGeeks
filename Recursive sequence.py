
class Solution:
    def sequence(self, N):
        # code here
        cnt=1
        ans=0
        i=1
        while i<=N:
            mul=1
            val=0
            while val<i:
                mul*=cnt
                cnt+=1
                val+=1
            ans+=mul 
            i+=1
        return ans
