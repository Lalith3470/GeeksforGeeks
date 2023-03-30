#User function Template for python3
from itertools import permutations
class Solution:
    def permutation(self,s):
        s=permutations(s)
        l=[]
        for i in s:
            l.append("".join(i))
        return sorted(l)
