class Solution:
    def search(self, patt, s):
        # code here
        if patt not in s:return [-1]
        lst=[]
        for i in range(0,len(s)-len(patt)+1):
            v=s[i:i+len(patt)]
            if v==patt:
                lst.append(i+1)
        return lst
