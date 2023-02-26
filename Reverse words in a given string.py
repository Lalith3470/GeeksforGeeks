class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        s=(S.split("."))[::-1]
        return ".".join(s)
        
