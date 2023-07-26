class Solution:
    def lookandsay(self, n):
        # code here
        if n==1:return "1"
        s="1"
        while n>1:
            tmp=[]
            st=[]
            cnt=0
            for i in s:
                if st and st[-1]==i:
                    cnt+=1
                else:
                    if cnt>0:
                        tmp.append([st[0],cnt])
                    cnt=1
                    st=[]
                    st.append(i)
            if st and cnt>0:
                tmp.append([st[0],cnt])
            lst=[]
            nstr=""
            for i,j in tmp:
                nstr+=str(i)+str(j)
            s=nstr
            n-=1
        return s[::-1]
