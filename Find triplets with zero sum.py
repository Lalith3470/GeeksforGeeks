class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        arr.sort()
        for i in range(n-2):
            lo=i+1
            hi=n-1
            target=-arr[i]
            while lo<hi:
                if arr[lo]+arr[hi]==target:
                    return True
                elif arr[lo]+arr[hi]>target:
                    hi-=1
                else:
                    lo+=1
        return False
