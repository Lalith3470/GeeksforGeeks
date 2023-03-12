from itertools import permutations
class Solution:
    def find_permutation(self, S):
        # Code here
        lst=[]
        for i in permutations(S):
            lst.append("".join(i))
        val=sorted([*set(lst)])
        return val
        
