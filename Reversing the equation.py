class Solution:
    def reverseEqn(self, s):
        # code here
        lst=[]
        c=''
        for i in s:
            if i.isnumeric():
                c+=i
            else:
                if c: 
                    lst.append(c)
                    c=''
                lst.append(i)
        if c:lst.append(c)
        return ''.join(lst[::-1])
