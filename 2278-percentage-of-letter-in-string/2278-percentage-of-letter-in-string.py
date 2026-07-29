class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count=0
        n=len(s)
        for ch in s:
            if ch==letter:
                count+=1
        return int((count/n)*100)
        