class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        # code here
        li.sort(reverse=True)
        return li[:k]
