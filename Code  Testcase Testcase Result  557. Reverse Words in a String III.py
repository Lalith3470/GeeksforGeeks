class Solution:
    def reverseWords(self, s: str) -> str:
        st=[]
        s=s.split()
        for i in range(len(s)):
            a=s[i]
            st.append(a[::-1])    
        return ' '.join(st)
