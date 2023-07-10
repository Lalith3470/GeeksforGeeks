class Solution:
    #Function to find transpose of a matrix.
    def transpose(self,matrix, n):
        lst=[]
        for i in zip(*matrix):
            lst.append(i)
        matrix[:]=lst
        return matrix
        
