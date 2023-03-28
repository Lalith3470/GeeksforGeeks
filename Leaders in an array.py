class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        lst=[A[-1]]
        A=A[::-1]
        for i in range(1,N):
            if lst[-1]<=A[i]:
                lst.append(A[i])
        return lst[::-1]
