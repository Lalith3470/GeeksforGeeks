#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        lst=arr1+arr2
        lst.sort()
        return lst[k-1]
