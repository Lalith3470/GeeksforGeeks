
class Solution:
    
    #Function to check if Kth bit is set or not.
    def checkKthBit(self, n,k):
        #Your code here
        res=bin(n)[2:][::-1]
        if res[k]=='1':
            return 1
        return 0
