from collections import Counter
class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        return sorted(a)==sorted(b)
