class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        upr=[]
        lor=[]
        for i in s:
            if i.isupper():upr.append(i)
            else:lor.append(i)
        upr.sort()
        lor.sort()
        cnt1,cnt2=0,0
        st=""
        for i in s:
            if i.isupper():
                st+=upr[cnt1]
                cnt1+=1
            else:
                st+=lor[cnt2]
                cnt2+=1
        return st
