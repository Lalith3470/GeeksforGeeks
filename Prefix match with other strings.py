
class Solution:
    def klengthpref(self,arr,n,k,s):
        # return list of words(str) found in the board
        if len(s)<k:return 0
        s=s[:k]
        cnt=0
        for i in arr:
            if i[:k]==s:cnt+=1
        return cnt
