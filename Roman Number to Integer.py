class Solution:
    def romanToDecimal(self, S): 
        m=0
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in S:
            m+=d[i]
        if 'IV' in S or 'IX' in S:
            m=m-2
        if 'XL' in S or 'XC' in S:
            m=m-20
        if 'CD' in S or 'CM' in S:
            m=m-200
        return m
