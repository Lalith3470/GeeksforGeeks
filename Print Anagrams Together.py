
class Solution:
    def Anagrams(self, words, n):
        lst=[]
        tmp=[]
        for i in words:
            s=''.join(sorted(i))
            if s in tmp:
                lst[tmp.index(s)].append(i)
            else:
                tmp.append(s)
                lst.append([i])
        return lst
