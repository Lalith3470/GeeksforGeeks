from typing import List
class Solution:
    def totalTime(self, n : int, arr : List[int], time : List[int]) -> int:
        # code here
        dic={}
        for i in range(n):
            dic[i+1]=time[i]
        sm=-1
        cnt={}
        for i in range(n):
            if arr[i] in cnt:
                sm+=dic[arr[i]]
            else:
                cnt[arr[i]]=1
                sm+=1
        return sm
