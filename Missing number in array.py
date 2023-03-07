class Solution:
    def MissingNumber(self,array,n):
        # code here
        lst=[i for i in range(1,n+1)]
        for i in (set(lst)^set(array)):
            return i
        
