from typing import List
from collections import Counter
class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        # code here
        tmp=arr.copy()
        tmp=sorted(set(tmp))
        dic={-1:0,0:0}
        sm=0
        v=Counter(arr)
        l={}
        for i in range(max(arr)+1):
            l[i]=i
        for i in range(len(tmp)):
            a=tmp[i]
            if a in v:
                a*=v[a]
            sm+=a
            dic[l[tmp[i]]]=sm
        lst=[]
        for i in range(max(arr)):
            if i not in dic:
                dic[i]=dic[i-1]
        for i in arr:
            lst.append(dic[i-1])
        return lst
