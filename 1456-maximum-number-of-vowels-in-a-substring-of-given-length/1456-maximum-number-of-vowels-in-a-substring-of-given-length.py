class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count=0
        for ch in range(k):
            if s[ch] in ['a','e','i','o','u']:
                vowel_count+=1
        max_vowel=vowel_count
        for ch in range(k,len(s)):
            if s[ch] in ['a','e','i','o','u']:
                vowel_count+=1
            if s[ch-k] in ['a','e','i','o','u']:
                vowel_count-=1
            max_vowel=max(max_vowel,vowel_count)
        return max_vowel
                
        