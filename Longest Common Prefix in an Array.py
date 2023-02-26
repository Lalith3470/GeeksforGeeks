class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        s=""
        for i in zip(*arr):
            if len(set(i))==1:
                s+=i[0]
            else:
                break
        if s:
            return s
        else:
            return -1

