class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count=0
        vowels={'a','e','i','o','u'}
        for ch in range(k):
            if s[ch] in vowels:
                vowel_count+=1
        max_vowel=vowel_count
        for ch in range(k,len(s)):
            if s[ch] in vowels:
                vowel_count+=1
            if s[ch-k] in vowels:
                vowel_count-=1
            max_vowel=max(max_vowel,vowel_count)
        return max_vowel
                
        