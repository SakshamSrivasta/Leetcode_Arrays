class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            result=[]
            a=b=0
            while a<len(word1) and b<len(word2):
                result.append(word1[a])
                result.append(word2[b])
                a+=1
                b+=1
            result.extend(word1[a:])
            result.extend(word2[b:])
            return ''.join(result)