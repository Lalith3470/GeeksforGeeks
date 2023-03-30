from typing import List


class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
        # code here
        sm=sum(A)
        A.sort()
        for i in A:
            if sm<=(N*i):return i
        return 
    
