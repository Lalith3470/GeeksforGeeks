class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here
        n=bin(n)[2:]
        s=[]
        n=[i for i in n]
        if len(n)%2!=0:
            n.insert(0,"0")
        for i in range(0,len(n),2):
            s+=(n[i:i+2])[::-1]
        return int("".join(s),2)
