#User function Template for python3

class Solution:
    def maxOnes (self, Mat, N, M):
        # code here 
        lst=[]
        mx=0
        for i in range(len(Mat)):
            val=Mat[i].count(1)
            mx=max(val,mx)
            lst.append(val)
        for i in range(len(lst)):
            if lst[i]==mx:
                return i
        return -1
