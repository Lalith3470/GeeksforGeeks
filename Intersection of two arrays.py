class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        
        #code here
        res=[]
        a=set(a)
        b=set(b)
        for item in a:
            if item in b:
                res.append(item)
        return len(res) 
