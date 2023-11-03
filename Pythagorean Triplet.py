class Solution:

	def checkTriplet(self,arr, n):
        s=set()
        for item in arr:
            s.add(item**2)
        for aa in s:
            for bb in s:
                if aa+bb in s:
                    return True
        return False
