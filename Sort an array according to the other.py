from collections import Counter
class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        # Your Code Here
        cnt=Counter(A1)
        cnt1=Counter(A2)
        lst=set(A2)^set(A1)
        l=[]
        for i in A2:
            l+=[i]*cnt[i]
        l1=[]
        for i in lst:
            l1+=[i]*cnt[i]
        l1.sort()
        return l+l1
