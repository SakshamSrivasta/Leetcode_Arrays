class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count=0
        vowels={'a','e','i','o','u'}
        for i in range(k):
            if s[i] in vowels:
                vowel_count+=1
        max_vowel=vowel_count
        for i in range(k,len(s)):
            if s[i] in vowels:
                vowel_count+=1
            if s[i-k] in vowels:
                vowel_count-=1
            max_vowel=max(max_vowel,vowel_count)
        return max_vowel
                
        