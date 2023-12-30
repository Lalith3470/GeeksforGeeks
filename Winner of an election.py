from collections import Counter
class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieve
        cnt=Counter(arr)
        mx=max(cnt.values())
        lst=[]
        for i,j in cnt.items():
            if j==mx:lst.append(i)
        val=sorted(lst)
        return [val[0],mx]
