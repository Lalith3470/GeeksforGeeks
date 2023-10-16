class Solution:
	def AllPossibleStrings(self, s):
	    def get_pset(s, subs, start):
	        if start < len(s):
	            get_pset(s, subs+s[start], start+1)
	            get_pset(s, subs, start+1)
	        else:
	            ans.append(subs)

        ans = []
        get_pset(s, '', 0)
        ans.pop(-1)
        return sorted(ans)
