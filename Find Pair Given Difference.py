#User function Template for python3

class Solution:

    def findPair(self, arr, L,N):
        #code here
        def bs(arr,a):
            i=0
            j=len(arr)-1
            while i<=j:
                m=(i+j)//2
                if arr[m]==a:
                    return True
                elif arr[m]>a:
                    j=m-1
                else:i=m+1
            return False
        arr.sort()
        for i in range(len(arr)):
            a=abs(N-arr[i])
            
            v=bs(arr[:i]+arr[i+1:],a)
            if v==True:
                return True
        return False
