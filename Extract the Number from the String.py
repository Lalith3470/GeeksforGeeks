class Solution:
    def ExtractNumber(self,S):
        #code here
        S=S.split()
        lst=[]
        for i in S:
            if i.isnumeric() and "9" not in i:lst.append(int(i))
        return max(lst) if lst else -1
