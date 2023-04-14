from typing import List


class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        # code here
        stk = []
        for i in range(N):
            if stk and stk[-1][0]==color[i] and stk[-1][1]==radius[i]:
                stk.pop()
            else:
                stk.append((color[i], radius[i]))

        return len(stk)
