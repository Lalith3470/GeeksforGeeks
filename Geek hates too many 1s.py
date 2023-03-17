class Solution:
    def noConseBits(self, n : int) -> int:
        # code here
        n=bin(n)
        c=0
        s=[]
        for i in range(2,len(n)):
            if n[i]=="1":
                c+=1
            else:
                if c>0:c=0
            s.append(n[i])
            if c==3:
                s[-1]="0"
                c=0
        return int("".join(s),2)
