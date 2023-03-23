#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        Val=sorted(set(A)&set(B)&set(C))
        return Val

