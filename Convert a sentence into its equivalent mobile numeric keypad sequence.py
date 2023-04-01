#User function Template for python3

class Solution:

    def printSequence(self,S):
        # code here
        dic={"A":"2"*1,"B":"2"*2,"C":"2"*3,"D":"3"*1,"E":"3"*2,"F":"3"*3,
             "G":"4"*1,"H":"4"*2,"I":"4"*3,"J":"5"*1,"K":"5"*2,"L":"5"*3,
             "M":"6"*1,"N":"6"*2,"O":"6"*3,"P":"7"*1,"Q":"7"*2,"R":"7"*3,"S":"7"*4,
             "T":"8"*1,"U":"8"*2,"V":"8"*3,"W":"9"*1,"X":"9"*2,"Y":"9"*3,"Z":"9"*4}
        st=""
        for i in range(len(S)):
            if S[i] in dic:
                st+=dic[S[i]]
            else:
                st+="0"
        return st
                
