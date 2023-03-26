#User function Template for python3
import math
class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        pro=1
        for i in nums:
            if i!=0:
                pro*=i
        right=1
        l=[]
        for i in nums:
            if i==0:
                l=len(l)*[0]
            else:
                pro=pro//i
            l.append(right*pro)
            right*=i
        return l
