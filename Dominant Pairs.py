from typing import List


class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        # code here
        i=0
        j=n//2
        l=arr[:n//2]
        m=arr[n//2:]
        l.sort()
        m.sort()
        arr=l+m
        cnt=0
        while i<n//2 and j<n:
            if arr[i]>=5*arr[j]:
                cnt+=n//2-i
                j+=1
            else:i+=1
        return cnt
        


