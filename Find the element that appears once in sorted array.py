#User function Template for python3
from collections import Counter
class Solution:
    def findOnce(self,arr : list, n : int):
        # Complete this function
        cnt=Counter(arr)
        
        for i,j in cnt.items():
            if j==1:
                return i
        return -1
