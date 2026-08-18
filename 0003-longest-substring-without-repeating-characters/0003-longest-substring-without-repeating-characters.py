class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash=[-1]*256
        l=0
        r=0
        max_len=0
        while r<len(s):
            if hash[ord(s[r])]>=l:
                l=hash[ord(s[r])]+1
            max_len=max(max_len,r-l+1)
            hash[ord(s[r])]=r
            r+=1
        return max_len
                        
        # l=0
        # longest=0
        # n=len(s)
        # sett=set()
        # for r in range(n):
        #     while s[r] in sett:
        #         sett.remove(s[l])
        #         l+=1
        #     w=(r-l)+1 #window size
        #     longest=max(w,longest)
        #     sett.add(s[r])
        # return longest
        