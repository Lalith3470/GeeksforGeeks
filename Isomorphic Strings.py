
class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        return len(set(str1))==len(set(str2))==len(set(zip(str1,str2)))

