from typing import List


class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        mn=2**31
        for i in range(N):
            mn=min(mn,(abs(cur-pos[i]))*time[i])
        return mn
