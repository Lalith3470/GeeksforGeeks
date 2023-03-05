#User function Template for python3

class Solution:
    def allPairs(self, A, B, N, M, X):
        # Your code goes here 
        lst=[]
        A.sort()
        B.sort()
        for i in A:
            sm=i
            for j in B:
                sm+=j
                if sm==X:
                    lst.append([i,j])
                sm-=j
        lst=sorted(lst,key=lambda x:x[0])
        return lst
        

