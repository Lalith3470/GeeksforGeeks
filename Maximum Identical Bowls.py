from typing import List
class Solution:
    def getMaximum(self, N : int, arr : List[int]) -> int:
        # code here
        if N==1:return 1
        sm=sum(arr)
        for i in range(N,0,-1):
            if sm%i==0:
                return i
        
