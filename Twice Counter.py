#User function Template for python3
from collections import Counter
class Solution:
    def countWords(self,List, n):
        #code here
        cnt=Counter(List)
        c=0
        for i,j in cnt.items():
            if j==2:c+=1
        return c
        
