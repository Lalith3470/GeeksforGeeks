#User function Template for python3
class Solution:

    def rowWithMax1s(self,arr, n, m):
        # code here
        mx=0
        row=-1
        for i in range(n):
            val=arr[i].count(1)
            if val>mx:
                mx=val
                row=i
        return row
