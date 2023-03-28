#User function Template for python3

class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        a.sort()
        b.sort(reverse=True)
        sm=0
        for i in range(n):
            sm+=a[i]*b[i]
        return sm
