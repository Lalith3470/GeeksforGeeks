class Solution:
    def subArraySum(self,arr, n, s): 
        #Write your code here
        start=0
        sm=arr[0]
        i=1
        while i<=n:
            while sm>s and start<i-1:
                sm-=arr[start]
                start+=1
            if sm==s:
                return [start+1,i]
            if i<n:
                sm+=arr[i]
            i+=1
        return [-1]
