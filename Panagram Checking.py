class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        st={}
        for i in s:
            i=i.lower()
            if i not in st and i.isalpha():
                st[i]=1
        return len(st)==26
