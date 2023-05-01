from collections import Counter
class Solution:
    def majorityElement(self, A, N):
        #Your code here
        cnt=Counter(A)
        for i,j in cnt.items():
            if j>N//2:return i
        return -1
