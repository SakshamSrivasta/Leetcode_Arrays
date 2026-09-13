from collections import Counter

class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        res = 0
        s = []
        count = Counter()
        
        for a in nums:
            while s and s[-1] > a:
                count[s.pop()] -= 1
            res += len(s) - count[a]
            s.append(a)
            count[a] += 1
            
        return res