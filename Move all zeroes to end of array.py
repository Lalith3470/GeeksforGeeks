
class Solution:
    def pushZerosToEnd(self,arr, n):
        # code here
        l=[]
        lst=[]
        for i in arr:
            if i==0:
                l.append(i)
            else:
                lst.append(i)
        arr[:]=lst+l
