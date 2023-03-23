#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        l1,l2=[],[]
        for i in arr:
            if i<0:l1.append(i)
            else:l2.append(i)
        l=[]
        mn=min(len(l1),len(l2))
        for i in range(mn):
            l.append(l2[i])
            l.append(l1[i])
        if mn==len(l1):
            l+=l2[mn:]
        else:l+=l1[mn:]
        arr[:]=l
