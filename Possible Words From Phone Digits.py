from itertools import product

class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,a,N):
        #Your code here
        dict={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if not a:
            return []
        lst=[]
        for i in a:
            i=str(i)
            if i in dict:
                lst.append(dict[i])
        ans=product(*lst)
        res=[]
        for i in ans:
            res.append(''.join(i))
        return res
