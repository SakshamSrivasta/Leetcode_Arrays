class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        freq=Counter(s[:n>>1])
        half="".join(c*freq[c] for c in ascii_lowercase)
        if n%2==0:
            return half + half[::-1]
        return half + s[n//2] +half[::-1]
       